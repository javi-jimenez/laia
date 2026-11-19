#!/usr/bin/env python3
"""Register the whitepapers in Zenodo through its REST API.

Zenodo (CERN) mints a DOI for every record, which is what makes a paper citable
and lets ORCID, Crossref-based services and Google Scholar resolve it. It is the
only repository in this list that accepts unpublished drafts over a plain API
and without institutional membership.

Safety: publishing a record is permanent. This script therefore

  * does nothing without a token (``ZENODO_TOKEN``),
  * defaults to *draft* mode — the record is created but stays private,
  * and only publishes, and only writes the DOI to ``whitepapers/dois.json``,
    when ``--publish`` is passed.

Usage:
    export ZENODO_TOKEN=...                     # zenodo.org/account/settings/applications
    python3 scripts/zenodo_publish.py --dry-run             # what would be sent
    python3 scripts/zenodo_publish.py                       # create drafts
    python3 scripts/zenodo_publish.py --only <slug>          # one paper
    python3 scripts/zenodo_publish.py --publish              # drafts + publish + record DOI
    python3 scripts/zenodo_publish.py --sandbox --publish    # same, on sandbox.zenodo.org

The PDF is taken from ``pdf/out/<slug>.pdf`` when present (run ``make pdfs``
first); the Markdown source is always uploaded alongside it.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from whitepaper_meta import REPO_ROOT, Paper, load_papers, numbered, split_name

PRODUCTION = "https://zenodo.org/api"
SANDBOX = "https://sandbox.zenodo.org/api"

DOIS_FILE = REPO_ROOT / "whitepapers" / "dois.json"
PDF_DIR = REPO_ROOT / "pdf" / "out"
WPS_DIR = REPO_ROOT / "whitepapers"

USER_AGENT = "laia-zenodo-publisher/1.0 (+https://laia.brisecom.org)"

# Token lookup order: env var, then this file (kept outside the repo so it can
# never be committed). The file only needs to contain the token. Sandbox uses
# its own file so a rehearsal cannot overwrite the production credentials.
TOKEN_DIR = Path.home() / ".config" / "laia"
DEFAULT_TOKEN_FILE = TOKEN_DIR / "zenodo.token"
SANDBOX_TOKEN_FILE = TOKEN_DIR / "zenodo.sandbox.token"

ABSTRACT_RE = re.compile(
    r"^##\s+Abstract\s*$(.*?)(?=^##\s)", re.MULTILINE | re.DOTALL | re.IGNORECASE
)


class ZenodoError(RuntimeError):
    pass


def request(
    method: str,
    url: str,
    token: str,
    payload: dict | None = None,
    data: bytes | None = None,
    content_type: str | None = None,
) -> dict:
    body = data
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    elif content_type:
        headers["Content-Type"] = content_type

    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:800]
        raise ZenodoError(f"{method} {url} -> HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise ZenodoError(f"{method} {url} -> {exc.reason}") from exc

    time.sleep(1)  # Zenodo asks for roughly one request per second
    return json.loads(raw) if raw else {}


def extract_abstract(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = ABSTRACT_RE.search(text)
    if not match:
        return ""
    paragraphs = " ".join(match.group(1).split())
    return paragraphs.strip()


def build_metadata(paper: Paper, abstract: str) -> dict:
    creators = []
    for author in paper.authors:
        family, given = author.family_given
        creator = {"name": f"{family}, {given}" if given else family}
        if author.orcid:
            creator["orcid"] = author.orcid
        creators.append(creator)

    metadata = {
        "title": paper.title,
        "upload_type": "publication",
        "publication_type": "technicalnote",
        "publication_date": paper.date,
        "description": abstract or f"{paper.title} ({paper.affiliation}).",
        "creators": creators,
        "access_right": "open",
        "license": "cc-by-nc-sa-4.0",
        "keywords": list(paper.keywords) or [paper.topic] if paper.topic else [],
        "version": paper.version or "1.0",
        "notes": f"{paper.affiliation} · {paper.status} · {paper.license}",
    }
    return metadata


def upload_file(bucket: str, path: Path, token: str) -> None:
    req = urllib.request.Request(
        f"{bucket}/{path.name}",
        data=path.read_bytes(),
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": USER_AGENT,
            "Content-Type": "application/octet-stream",
        },
        method="PUT",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as response:
            response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:800]
        raise ZenodoError(f"upload {path.name} -> HTTP {exc.code}: {detail}") from exc
    time.sleep(1)


def load_dois() -> dict[str, dict[str, object]]:
    if not DOIS_FILE.exists():
        return {}
    return json.loads(DOIS_FILE.read_text(encoding="utf-8"))


def save_dois(dois: dict[str, dict[str, object]]) -> None:
    DOIS_FILE.write_text(
        json.dumps(dict(sorted(dois.items())), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def resolve_token(token_file: str | None, sandbox: bool) -> str:
    """Read the token from ZENODO_TOKEN, then from the environment's file."""
    token = os.environ.get("ZENODO_TOKEN", "").strip()
    if token:
        return token
    if token_file:
        path = Path(token_file).expanduser()
    else:
        path = SANDBOX_TOKEN_FILE if sandbox else DEFAULT_TOKEN_FILE
    if path.is_file():
        return path.read_text(encoding="utf-8").strip()
    return ""


def default_token_path(sandbox: bool) -> Path:
    return SANDBOX_TOKEN_FILE if sandbox else DEFAULT_TOKEN_FILE


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create (and optionally publish) Zenodo records for the whitepapers."
    )
    parser.add_argument("--only", help="process a single slug")
    parser.add_argument(
        "--publish",
        action="store_true",
        help="publish the records (PERMANENT) and record their DOIs",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the metadata that would be sent; no network calls",
    )
    parser.add_argument(
        "--sandbox", action="store_true", help="use sandbox.zenodo.org instead of production"
    )
    parser.add_argument(
        "--token-file",
        help="file containing the token (default: ~/.config/laia/zenodo[.sandbox].token)",
    )
    args = parser.parse_args()

    papers = numbered(load_papers())
    dois = load_dois()

    selected = [(n, p) for n, p in papers if not args.only or p.slug == args.only]
    if not selected:
        raise SystemExit(f"error: no whitepaper matches '{args.only}'")

    pending = [(n, p) for n, p in selected if p.slug not in dois]
    already = [p.slug for _, p in selected if p.slug in dois]

    if already:
        print(f"already registered (skipped): {', '.join(already)}")
    if not pending:
        print("Nothing to do: every selected whitepaper has a DOI.")
        return 0

    if args.dry_run:
        for number, paper in pending:
            abstract = extract_abstract(WPS_DIR / f"{paper.slug}.md")
            print(f"\n=== WP {number:02d} {paper.slug}")
            print(json.dumps(build_metadata(paper, abstract), ensure_ascii=False, indent=2))
            pdf = PDF_DIR / f"{paper.slug}.pdf"
            print(f"files: {paper.slug}.md" + (f", {pdf.name}" if pdf.exists() else " (no PDF)"))
        print("\n(dry run: nothing sent)")
        return 0

    token = resolve_token(args.token_file, args.sandbox)
    if not token:
        location = (
            "https://sandbox.zenodo.org/account/settings/applications/"
            if args.sandbox
            else "https://zenodo.org/account/settings/applications/"
        )
        target = (
            Path(args.token_file).expanduser()
            if args.token_file
            else default_token_path(args.sandbox)
        )
        raise SystemExit(
            "error: no Zenodo token found.\n"
            f"  Create one at {location} (scopes: deposit:write, deposit:actions)\n"
            f"  then either export ZENODO_TOKEN=... or save it with:\n"
            f"    mkdir -p {target.parent} && chmod 700 {target.parent}\n"
            f"    printf '%s' TOKEN > {target} && chmod 600 {target}"
        )

    api = SANDBOX if args.sandbox else PRODUCTION
    failures = 0

    for number, paper in pending:
        label = f"WP {number:02d} {paper.slug}"
        pdf = PDF_DIR / f"{paper.slug}.pdf"
        try:
            abstract = extract_abstract(WPS_DIR / f"{paper.slug}.md")
            print(f"▶ {label}: creating draft…")
            deposition = request(
                "POST",
                f"{api}/deposit/depositions",
                token,
                payload={},
            )
            dep_id = deposition["id"]
            bucket = deposition["links"]["bucket"]

            request(
                "PUT",
                f"{api}/deposit/depositions/{dep_id}",
                token,
                payload={"metadata": build_metadata(paper, abstract)},
            )

            upload_file(bucket, WPS_DIR / f"{paper.slug}.md", token)
            if pdf.exists():
                upload_file(bucket, pdf, token)
            else:
                print(f"  ! no PDF at {pdf.relative_to(REPO_ROOT)} (run `make pdfs`)")

            if not args.publish:
                url = deposition["links"].get("html", f"https://zenodo.org/deposit/{dep_id}")
                print(f"  draft kept private: {url}")
                print("  publish with --publish once the metadata and files are right")
                continue

            record = request(
                "POST",
                f"{api}/deposit/depositions/{dep_id}/actions/publish",
                token,
            )
            doi = record.get("doi") or record.get("metadata", {}).get("doi")
            dois[paper.slug] = {
                "doi": doi,
                "zenodoRecord": record.get("id", dep_id),
                "publishedAt": record.get("created", ""),
                "environment": "sandbox" if args.sandbox else "production",
            }
            save_dois(dois)
            print(f"  ✔ published: {doi}")
        except ZenodoError as exc:
            failures += 1
            print(f"  ✖ {label}: {exc}", file=sys.stderr)

    if args.publish and pending:
        print("\nNext: `make citations` to propagate the DOIs into CITATION.cff and the BibTeX.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
