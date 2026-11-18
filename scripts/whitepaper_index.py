#!/usr/bin/env python3
"""Regenerate the whitepaper index tables of the repository.

The front matter of every file in ``whitepapers/`` is the single source of
truth. This script reads it and rewrites the table blocks delimited by the
markers below in:

  * ``README.md``               (project home, short table)
  * ``whitepapers/README.md``   (full index, with topic and status)

Usage:
    python3 scripts/whitepaper_index.py            # rewrite the tables
    python3 scripts/whitepaper_index.py --check    # exit 1 if out of date

Front matter fields used:

  order    Integer rank shown in the "#" column. Optional: papers without it
           are appended at the end, sorted by date. Other papers reference it
           as "WP <order>", so values must stay stable.
  topic    Short description for the "Topic" column. Optional: falls back to
           the first tags.
  status   Publication status, defaults to "Draft".
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WHITEPAPERS_DIR = REPO_ROOT / "whitepapers"
GITHUB_REPO = "javi-jimenez/laia"
PDF_URL = f"https://github.com/{GITHUB_REPO}/releases/latest/download/{{slug}}.pdf"

START = "<!-- whitepapers-index:start -->"
END = "<!-- whitepapers-index:end -->"

KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")


@dataclass(frozen=True)
class Paper:
    slug: str
    title: str
    date: str
    status: str
    topic: str
    order: int | None

    @property
    def sort_key(self) -> tuple:
        if self.order is not None:
            return (0, self.order, "", self.slug)
        return (1, 0, self.date, self.slug)


def parse_front_matter(text: str) -> dict[str, object]:
    if not text.startswith("---"):
        return {}
    fields: dict[str, object] = {}
    for line in text.splitlines()[1:]:
        if line.strip() == "---":
            return fields
        match = KEY_RE.match(line)
        if not match:
            continue
        key, raw = match.group(1), match.group(2).strip()
        if raw.startswith("[") and raw.endswith("]"):
            items = [item.strip().strip("\"'") for item in raw[1:-1].split(",")]
            fields[key] = [item for item in items if item]
        else:
            fields[key] = raw.strip("\"'")
    raise ValueError("unterminated front matter")


def load_papers() -> list[Paper]:
    papers: list[Paper] = []
    for path in sorted(WHITEPAPERS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        fields = parse_front_matter(path.read_text(encoding="utf-8"))
        title = str(fields.get("title", "")).strip()
        date = str(fields.get("date", "")).strip()
        if not title or not date:
            raise SystemExit(
                f"error: {path.name} needs 'title' and 'date' in its front matter"
            )

        topic = str(fields.get("topic", "")).strip()
        if not topic:
            tags = fields.get("tags") or fields.get("keywords") or []
            if isinstance(tags, list):
                topic = ", ".join(tags[:4])

        raw_order = str(fields.get("order", "")).strip()
        order = int(raw_order) if raw_order.isdigit() else None

        papers.append(
            Paper(
                slug=path.stem,
                title=title,
                date=date,
                status=str(fields.get("status", "Draft")).strip() or "Draft",
                topic=topic,
                order=order,
            )
        )

    seen: dict[int, str] = {}
    for paper in papers:
        if paper.order is None:
            continue
        if paper.order in seen:
            raise SystemExit(
                f"error: duplicate order {paper.order} in "
                f"'{seen[paper.order]}' and '{paper.slug}'"
            )
        seen[paper.order] = paper.slug

    return sorted(papers, key=lambda paper: paper.sort_key)


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|")


def render_full_index(papers: list[Paper]) -> str:
    rows = [
        "| # | Document | Topic | Date | Status | PDF |",
        "|---|----------|-------|------|--------|-----|",
    ]
    for number, paper in enumerate(papers, start=1):
        rows.append(
            f"| {number:02d} | [{escape_cell(paper.title)}]({paper.slug}.md) "
            f"| {escape_cell(paper.topic)} | {paper.date} | {paper.status} "
            f"| [PDF]({PDF_URL.format(slug=paper.slug)}) |"
        )
    return "\n".join(rows)


def render_home_index(papers: list[Paper]) -> str:
    rows = [
        "| # | Documento | Fecha | PDF |",
        "|---|-----------|-------|-----|",
    ]
    for number, paper in enumerate(papers, start=1):
        rows.append(
            f"| {number:02d} | "
            f"[{escape_cell(paper.title)}](whitepapers/{paper.slug}.md) "
            f"| {paper.date} | [PDF]({PDF_URL.format(slug=paper.slug)}) |"
        )
    return "\n".join(rows)


TARGETS = {
    "README.md": render_home_index,
    "whitepapers/README.md": render_full_index,
}


def update(path: Path, table: str, write: bool) -> bool:
    """Return True if the file is out of date; write it unless ``write`` is False."""
    text = path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(
            f"error: {path.name} is missing the index markers {START} / {END}"
        )
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new_text = f"{head}{START}\n{table}\n{END}{tail}"
    if new_text == text:
        return False
    if write:
        path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the whitepaper index tables from front matter."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not write; exit 1 if any index is out of date",
    )
    args = parser.parse_args()

    papers = load_papers()
    if not papers:
        raise SystemExit("error: no whitepapers found")

    changed = [
        name
        for name, render in TARGETS.items()
        if update(REPO_ROOT / name, render(papers), write=not args.check)
    ]

    if args.check:
        if changed:
            print("Whitepaper index is out of date in: " + ", ".join(changed))
            print("Run: make index")
            return 1
        print(f"Whitepaper index is up to date ({len(papers)} documents).")
        return 0

    if changed:
        print(f"Updated {len(papers)} whitepaper entries in: " + ", ".join(changed))
    else:
        print(f"Whitepaper index already up to date ({len(papers)} documents).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
