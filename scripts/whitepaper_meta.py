#!/usr/bin/env python3
"""Shared metadata layer for the whitepaper tooling.

The YAML front matter of ``whitepapers/*.md`` is the single source of truth for
everything the project publishes about a paper: its index row, its citation
entry and its PDF asset name. This module parses it once so the generators
(``whitepaper_index.py``, ``whitepaper_citations.py``) cannot disagree.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WHITEPAPERS_DIR = REPO_ROOT / "whitepapers"

GITHUB_REPO = "javi-jimenez/laia"
BLOB_URL = f"https://github.com/{GITHUB_REPO}/blob/main/whitepapers/{{slug}}.md"
PDF_URL = f"https://github.com/{GITHUB_REPO}/releases/latest/download/{{slug}}.pdf"

KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")


@dataclass(frozen=True)
class Paper:
    slug: str
    title: str
    date: str
    status: str
    topic: str
    order: int | None
    authors: tuple[str, ...]
    keywords: tuple[str, ...]
    version: str
    license: str
    affiliation: str

    @property
    def sort_key(self) -> tuple:
        if self.order is not None:
            return (0, self.order, "", self.slug)
        return (1, 0, self.date, self.slug)

    @property
    def url(self) -> str:
        return BLOB_URL.format(slug=self.slug)

    @property
    def pdf_url(self) -> str:
        return PDF_URL.format(slug=self.slug)

    @property
    def year(self) -> str:
        return self.date[:4]

    @property
    def citation_id(self) -> str:
        return f"laia-{self.slug}"


def parse_front_matter(text: str) -> dict[str, object]:
    """Parse the flat, scalar-or-list YAML subset used by the whitepapers."""
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


def _as_tuple(value: object) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(value)
    if isinstance(value, str) and value:
        return (value,)
    return ()


def load_papers() -> list[Paper]:
    """Return the papers sorted by their declared order, then by date."""
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
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            raise SystemExit(
                f"error: {path.name} has date '{date}'; expected YYYY-MM-DD"
            )

        topic = str(fields.get("topic", "")).strip()
        if not topic:
            fallback = _as_tuple(fields.get("tags")) or _as_tuple(fields.get("keywords"))
            topic = ", ".join(fallback[:4])

        raw_order = str(fields.get("order", "")).strip()
        if raw_order and not raw_order.isdigit():
            raise SystemExit(
                f"error: {path.name} has non-numeric order '{raw_order}'"
            )

        papers.append(
            Paper(
                slug=path.stem,
                title=title,
                date=date,
                status=str(fields.get("status", "Draft")).strip() or "Draft",
                topic=topic,
                order=int(raw_order) if raw_order else None,
                authors=_as_tuple(fields.get("authors")) or (
                    "Francisco Javier Jiménez Gómez",
                ),
                keywords=_as_tuple(fields.get("keywords"))
                or _as_tuple(fields.get("tags")),
                version=str(fields.get("version", "")).strip(),
                license=str(fields.get("license", "CC BY-NC-SA 4.0")).strip(),
                affiliation=str(
                    fields.get("affiliation", "Brisecom / LAIA Project")
                ).strip(),
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


def numbered(papers: list[Paper]) -> list[tuple[int, Paper]]:
    """Pair each paper with the number shown as "WP <n>".

    Declared orders win. Papers without one are given the next free number, so
    the index, the BibTeX keys and the cross-references always agree.
    """
    used = {paper.order for paper in papers if paper.order is not None}
    next_free = max(used, default=0) + 1
    result: list[tuple[int, Paper]] = []
    for paper in papers:
        if paper.order is not None:
            result.append((paper.order, paper))
            continue
        while next_free in used:
            next_free += 1
        used.add(next_free)
        result.append((next_free, paper))
        next_free += 1
    return result


def split_name(full_name: str) -> tuple[str, str]:
    """Split "Francisco Javier Jiménez Gómez" into (family, given)."""
    parts = full_name.split()
    if len(parts) < 2:
        return full_name, ""
    return " ".join(parts[-2:]), " ".join(parts[:-2])
