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

Front matter fields used: ``title``, ``date``, ``status``, ``order``, ``topic``
(see ``scripts/whitepaper_meta.py`` for the full schema).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from whitepaper_meta import REPO_ROOT, Paper, load_papers, numbered

START = "<!-- whitepapers-index:start -->"
END = "<!-- whitepapers-index:end -->"


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|")


def render_full_index(papers: list[tuple[int, Paper]]) -> str:
    rows = [
        "| # | Document | Topic | Date | Status | PDF |",
        "|---|----------|-------|------|--------|-----|",
    ]
    for number, paper in papers:
        rows.append(
            f"| {number:02d} | [{escape_cell(paper.title)}]({paper.slug}.md) "
            f"| {escape_cell(paper.topic)} | {paper.date} | {paper.status} "
            f"| [PDF]({paper.pdf_url}) |"
        )
    return "\n".join(rows)


def render_home_index(papers: list[tuple[int, Paper]]) -> str:
    rows = [
        "| # | Documento | Fecha | PDF |",
        "|---|-----------|-------|-----|",
    ]
    for number, paper in papers:
        rows.append(
            f"| {number:02d} | "
            f"[{escape_cell(paper.title)}](whitepapers/{paper.slug}.md) "
            f"| {paper.date} | [PDF]({paper.pdf_url}) |"
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

    papers = numbered(load_papers())
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
