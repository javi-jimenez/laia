#!/usr/bin/env bash
#
# generate_pdfs.sh
# ----------------
# Genera los PDFs de los whitepapers de LAIA a partir de los archivos Markdown,
# usando pandoc + xelatex. Usa la plantilla por defecto de pandoc (que maneja
# correctamente los bloques de código) y añade la portada de marca de LAIA
# (pdf/cover.tex) mediante --include-before-body.
#
# Uso:
#   ./pdf/generate_pdfs.sh            # genera todos los PDFs en pdf/out/
#   ./pdf/generate_pdfs.sh <archivo>  # genera solo un whitepaper
#
# Requisitos: pandoc, xelatex (TeX Live).
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WP_DIR="$REPO_ROOT/whitepapers"
OUT_DIR="$SCRIPT_DIR/out"
COVER="$SCRIPT_DIR/cover.tex"

mkdir -p "$OUT_DIR"

# Extrae el valor de un campo del front matter YAML de un archivo Markdown.
# Devuelve el texto tras "key:" eliminando comillas de apertura/cierre.
get_meta() {
  local file="$1"
  local key="$2"
  # Busca la línea "key: valor" y extrae el valor tras el primer ": ".
  grep -m1 -E "^${key}:" "$file" \
    | sed -E "s/^${key}:[[:space:]]*//" \
    | sed -E 's/^["'"'"']|["'"'"']$//g'
}

generate_one() {
  local md="$1"
  local base
  base="$(basename "$md" .md)"
  local title subtitle author date out
  local args=()

  title="$TITLE"
  if [ -z "$title" ]; then
    title="$(get_meta "$md" "title")"
  fi
  subtitle="${SUBTITLE:-A Whitepaper by LAIA and Brisecom}"
  author="${AUTHOR:-Brisecom / LAIA Project}"
  date="${DATE:-}"
  out="$OUT_DIR/$base.pdf"

  args=(
    "$md"
    --from markdown+raw_html
    --to pdf
    --pdf-engine=xelatex
    --include-before-body="$COVER"
    -o "$out"
  )
  if [ -n "$title" ]; then
    args+=(--metadata "title=$title")
  fi
  args+=(--metadata "subtitle=$subtitle")
  args+=(--metadata "author=$author")
  if [ -n "$date" ]; then
    args+=(--metadata "date=$date")
  fi

  echo "▶ Generando: $base.pdf"
  pandoc "${args[@]}"

  echo "  ✔ $out"
}

# Si se pasa un archivo concreto, generar solo ese.
if [ "$#" -ge 1 ]; then
  TITLE="${TITLE:-}"
  SUBTITLE="${SUBTITLE:-}"
  AUTHOR="${AUTHOR:-}"
  DATE="${DATE:-}"
  generate_one "$1"
  echo "Listo."
  exit 0
fi

# Generar todos los whitepapers.
for md in "$WP_DIR"/*.md; do
  [ "$(basename "$md")" = "README.md" ] && continue
  TITLE="$(get_meta "$md" "title")"
  generate_one "$md"
done

echo ""
echo "✅ PDFs generados en: $OUT_DIR"
