#!/usr/bin/env python3
"""Propaga los DOIs de whitepapers/dois.json al propio whitepaper.

Por qué: el DOI vive en un registro aparte, así que quien abre el .md en
GitHub no lo ve. GitHub no permite metaetiquetas por fichero en Markdown, de
modo que la única forma de que se lea ahí es dejarlo escrito en el documento:

  1. `doi:` en el front matter (lo lee cualquier parser y el índice).
  2. Un bloque visible tras el título, entre marcadores HTML para poder
     actualizarlo o retirarlo sin ambigüedad.

Uso:
    python3 scripts/whitepaper_dois.py            # aplica
    python3 scripts/whitepaper_dois.py --check    # exit 1 si hay drift
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from whitepaper_meta import REPO_ROOT, WHITEPAPERS_DIR

DOIS_FILE = WHITEPAPERS_DIR / "dois.json"
START = "<!-- doi:start -->"
END = "<!-- doi:end -->"
DOI_RE = re.compile(r'^doi:\s*"?([^"\n]+)"?\s*$', re.MULTILINE)


def load_dois() -> dict:
    if not DOIS_FILE.exists():
        return {}
    return json.loads(DOIS_FILE.read_text(encoding="utf-8"))


def block_for(doi: str, extra: dict) -> str:
    concept = extra.get("conceptDoi")
    line = f"> **DOI:** [{doi}](https://doi.org/{doi}) · Zenodo"
    if concept:
        line += f" (concept DOI [{concept}](https://doi.org/{concept}))"
    line += " · cite this version"
    return f"{START}\n{line}\n{END}"


def set_front_matter_doi(text: str, doi: str | None) -> str:
    head, sep, rest = text.partition("\n---\n")
    if not sep:
        raise ValueError("no front matter")
    lines = head.splitlines()
    has = any(line.startswith("doi:") for line in lines)
    if doi:
        entry = f'doi: "{doi}"'
        if has:
            lines = [entry if line.startswith("doi:") else line for line in lines]
        else:
            # junto a los otros identificadores del documento
            idx = next(
                (i for i, line in enumerate(lines) if line.startswith("license:")),
                len(lines),
            )
            lines.insert(idx, entry)
    elif has:
        lines = [line for line in lines if not line.startswith("doi:")]
    return "\n".join(lines) + sep + rest


def set_block(text: str, block: str | None) -> str:
    if START in text and END in text:
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        text = head + (block if block else "") + tail
        return re.sub(r"\n{3,}", "\n\n", text)

    if not block:
        return text

    # Insertar tras el primer H1 (y su línea en blanco), o al principio.
    match = re.search(r"^# .+$", text, re.MULTILINE)
    if not match:
        return text
    insert_at = match.end()
    return text[:insert_at] + "\n\n" + block + text[insert_at:]


def main() -> int:
    ap = argparse.ArgumentParser(description="Copia los DOIs al whitepaper.")
    ap.add_argument("--check", action="store_true", help="no escribe; exit 1 si difiere")
    args = ap.parse_args()

    dois = load_dois()
    changed: list[str] = []

    for path in sorted(WHITEPAPERS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        before = path.read_text(encoding="utf-8")
        entry = dois.get(path.stem) or {}
        doi = entry.get("doi")

        after = set_front_matter_doi(before, doi)
        after = set_block(after, block_for(doi, entry) if doi else None)

        if after == before:
            continue
        changed.append(path.name)
        if not args.check:
            path.write_text(after, encoding="utf-8")

    if args.check:
        if changed:
            print(f"✗ {len(changed)} whitepaper(s) sin el DOI en el documento:")
            for name in changed:
                print(f"   - {name}")
            print("  Ejecuta: make dois")
            return 1
        print(f"✓ los {len(dois)} DOIs están en su whitepaper")
        return 0

    if changed:
        print(f"✓ DOI escrito en {len(changed)} whitepaper(s)")
    else:
        print(f"✓ los {len(dois)} DOIs ya estaban en su whitepaper")
    return 0


if __name__ == "__main__":
    sys.exit(main())
