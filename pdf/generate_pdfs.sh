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

# Escapa caracteres especiales de LaTeX en un valor.
latex_escape() {
  printf '%s' "$1" \
    | sed -E 's/\\/\\textbackslash{}/g; s/&/\\&/g; s/%/\\%/g; s/\$/\\$/g; s/#/\\#/g; s/_/\\_/g; s/\{/\\{/g; s/\}/\\}/g; s/~/\textasciitilde{}/g; s/\^/\textasciicircum{}/g'
}

# Escapa caracteres especiales de LaTeX (para insertar texto en la portada).
latex_escape() {
  printf '%s' "$1" \
    | perl -pe 's/\\/\\textbackslash{}/g; s/&/\\&/g; s/%/\\%/g; s/\$/\\\$/g; s/#/\\#/g; s/_/\\_/g; s/\{/\\{/g; s/\}/\\}/g; s/~/\\textasciitilde{}/g; s/\^/\\textasciicircum{}/g'
}

# Genera una portada temporal con las variables $title$, $subtitle$, $author$
# resueltas (pandoc NO sustituye variables en --include-before-body).
# Usa perl para manejar correctamente caracteres especiales (&, $, etc.).
make_cover() {
  local title subtitle author
  title="$(latex_escape "$1")"
  subtitle="$(latex_escape "$2")"
  author="$(latex_escape "$3")"
  TITLE="$title" SUBTITLE="$subtitle" AUTHOR="$author" perl -pe '
    s/\$title\$/$ENV{TITLE}/g;
    s/\$subtitle\$/$ENV{SUBTITLE}/g;
    s/\$author\$/$ENV{AUTHOR}/g;
  ' "$COVER"
}

generate_one() {
  local md="$1"
  local base
  base="$(basename "$md" .md)"
  local title subtitle author date out cover_tmp
  local args=()

  title="$TITLE"
  if [ -z "$title" ]; then
    title="$(get_meta "$md" "title")"
  fi
  subtitle="${SUBTITLE:-A Whitepaper by LAIA and Brisecom}"
  author="${AUTHOR:-Brisecom / LAIA Project}"
  date="${DATE:-}"
  out="$OUT_DIR/$base.pdf"

  # Generar la portada con las variables resueltas.
  cover_tmp="$(mktemp --suffix=.tex)"
  make_cover "$title" "$subtitle" "$author" > "$cover_tmp"

  # NOTA: NO pasamos title/subtitle/author como --metadata a pandoc, porque la
  # plantilla por defecto generaría una segunda portada con esos metadatos.
  # La portada ya se genera en cover_tmp con las variables resueltas.
  # Con --variable title/subtitle/author vacíos evitamos que la plantilla por
  # defecto genere su propia portada.
  args=(
    "$md"
    --from markdown+raw_html
    --to pdf
    --pdf-engine=xelatex
    --variable title=""
    --variable subtitle=""
    --variable author=""
    --include-before-body="$cover_tmp"
    -o "$out"
  )
  if [ -n "$date" ]; then
    args+=(--metadata "date=$date")
  fi

  echo "▶ Generando: $base.pdf"
  pandoc "${args[@]}"
  rm -f "$cover_tmp"

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
