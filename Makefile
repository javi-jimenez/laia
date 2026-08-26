# ============================================================
#  LAIA — Makefile
#  Generación de PDFs de whitepapers y tareas del proyecto.
# ============================================================

SHELL := /bin/bash

# ---------- Variables ----------
PDF_DIR   := pdf
OUT_DIR   := $(PDF_DIR)/out
WP_DIR    := whitepapers

PANDOC    ?= pandoc
XELATEX   ?= xelatex

# ---------- Ayuda ----------
.PHONY: help
help:
	@echo "LAIA — Inteligencia Artificial Ética"
	@echo ""
	@echo "Objetivos disponibles:"
	@echo "  make deps        Instala dependencias (pandoc + TeX Live) en Ubuntu"
	@echo "  make pdfs        Genera los PDFs de todos los whitepapers"
	@echo "  make pdf-one     Genera un PDF concreto (WP=whitepapers/<archivo>.md)"
	@echo "  make clean       Elimina los PDFs generados"
	@echo "  make check       Verifica que las dependencias están instaladas"
	@echo ""
	@echo "Ejemplo de un solo PDF:"
	@echo "  make pdf-one WP=whitepapers/acs-assistant-context-standard.md"

# ---------- Dependencias (Ubuntu) ----------
.PHONY: deps
deps:
	@echo "▶ Instalando dependencias para la generación de PDFs..."
	sudo apt-get update
	sudo apt-get install -y pandoc texlive-xetex texlive-latex-base \
		texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended \
		texlive-fonts-extra lmodern
	@echo "✅ Dependencias instaladas."

# ---------- Verificación ----------
.PHONY: check
check:
	@command -v $(PANDOC) >/dev/null 2>&1 || { echo "❌ pandoc no está instalado. Ejecuta: make deps"; exit 1; }
	@command -v $(XELATEX) >/dev/null 2>&1 || { echo "❌ xelatex no está instalado. Ejecuta: make deps"; exit 1; }
	@echo "✅ Dependencias disponibles: $(PANDOC) y $(XELATEX)."

# ---------- Generar todos los PDFs ----------
.PHONY: pdfs
pdfs: check
	@mkdir -p $(OUT_DIR)
	@bash $(PDF_DIR)/generate_pdfs.sh
	@echo ""
	@echo "✅ PDFs generados en $(OUT_DIR)/"

# ---------- Generar un único PDF ----------
.PHONY: pdf-one
pdf-one: check
	@test -n "$(WP)" || { echo "❌ Usa: make pdf-one WP=whitepapers/<archivo>.md"; exit 1; }
	@test -f "$(WP)" || { echo "❌ No existe: $(WP)"; exit 1; }
	@mkdir -p $(OUT_DIR)
	@bash $(PDF_DIR)/generate_pdfs.sh "$(WP)"
	@echo ""
	@echo "✅ PDF generado en $(OUT_DIR)/"

# ---------- Limpiar ----------
.PHONY: clean
clean:
	@rm -rf $(OUT_DIR)
	@echo "✔ Directorio $(OUT_DIR)/ eliminado."
