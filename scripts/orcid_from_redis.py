#!/usr/bin/env python3
"""Sync whitepapers/authors.json from the cluster config in Redis.

The cluster keeps non-secret shared values in Redis (see the
``brisecom-config`` repo); the author ORCID lives at
``config:laia:author_orcid``. This script pulls it from there so the
identifier is written once for the whole cluster instead of per repo.

Usage:
    python3 scripts/orcid_from_redis.py                  # apply
    python3 scripts/orcid_from_redis.py --check           # exit 1 if it differs
    REDIS_HOST=redis.service.consul python3 scripts/orcid_from_redis.py

Reads with ``redis-cli`` (no Python dependency); the key host is taken from
``REDIS_HOST``/``REDIS_PORT``, defaulting to the cluster service name.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from whitepaper_meta import AUTHORS_FILE, valid_orcid

REDIS_HOST = os.environ.get("REDIS_HOST", "redis.service.consul")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")

KEYS = {
    "orcid": "config:laia:author_orcid",
    "affiliation": "config:laia:author_affiliation",
    "name": "config:laia:author_name",
}
DEFAULT_AUTHOR = "Francisco Javier Jiménez Gómez"


def redis_get(key: str) -> str:
    if not shutil.which("redis-cli"):
        raise SystemExit(
            "error: redis-cli no está instalado (apt install redis-tools)"
        )
    result = subprocess.run(
        ["redis-cli", "-h", REDIS_HOST, "-p", REDIS_PORT, "GET", key],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if result.returncode != 0:
        raise SystemExit(
            f"error: no se pudo consultar Redis ({REDIS_HOST}:{REDIS_PORT}): "
            + (result.stderr.strip() or f"exit {result.returncode}")
        )
    value = result.stdout.strip()
    if value in ("", "(nil)"):
        raise SystemExit(f"error: la clave {key} no existe en Redis")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="no escribe; exit 1 si difiere"
    )
    args = parser.parse_args()

    author = redis_get(KEYS["name"]) if KEYS["name"] else DEFAULT_AUTHOR
    orcid = redis_get(KEYS["orcid"])
    affiliation = redis_get(KEYS["affiliation"])

    if not valid_orcid(orcid):
        raise SystemExit(f"error: Redis devolvió un ORCID no válido: {orcid}")

    current = json.loads(AUTHORS_FILE.read_text(encoding="utf-8")) if AUTHORS_FILE.exists() else {}
    current[author] = {"orcid": orcid, "affiliation": affiliation}
    updated = json.dumps(dict(sorted(current.items())), ensure_ascii=False, indent=2) + "\n"
    previous = AUTHORS_FILE.read_text(encoding="utf-8") if AUTHORS_FILE.exists() else ""

    if updated == previous:
        print(f"authors.json ya coincide con Redis ({orcid}).")
        return 0
    if args.check:
        print(f"authors.json difiere de Redis ({orcid}). Ejecuta: make orcid-sync")
        return 1

    AUTHORS_FILE.write_text(updated, encoding="utf-8")
    print(f"authors.json actualizado desde Redis: {orcid}")
    print("Siguiente: make index citations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
