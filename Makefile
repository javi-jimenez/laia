# ============================================================
#  LAIA — Makefile
#  Generación de PDFs de whitepapers y tareas del proyecto.
# ============================================================

SHELL := /bin/bash

# ---------- Variables ----------
empty :=
space := $(empty) $(empty)

REPO_ROOT := $(CURDIR)
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
	@echo "  make release     Genera los PDFs y crea un Release de GitHub (TAG=..., NOTES=...)"
	@echo "  make clean       Elimina los PDFs generados"
	@echo "  make check       Verifica que las dependencias están instaladas"
	@echo ""
	@echo "Ejemplo de un solo PDF:"
	@echo "  make pdf-one WP=whitepapers/acs-assistant-context-standard.md"
	@echo ""
	@echo "Ejemplos de release:"
	@echo "  make release TAG=v1.0.0 NOTES=\"LAIA Whitepapers v1.0\""
	@echo "  make release   (usa TAG vX.Y.Z y NOTES por defecto)"

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

# ---------- Crear Release de GitHub ----------
# Genera los PDFs y crea un release con:
#   - Un zip con los documentos .md de la raíz (Proyecto-IA-*.md + README).
#   - Un zip con los whitepapers .md.
#   - Los PDFs de los whitepapers como assets.
# El tag usa el patrón de los releases históricos: AAAAMMDDHHMM-Nombre
# (ej. 202608270110-LAIA-Whitepapers). Uso: make release NAME="nombre"
.PHONY: release
release: pdfs
	@command -v gh >/dev/null 2>&1 || { echo "❌ gh CLI no está instalado. Instala con: sudo apt install gh"; exit 1; }
	@gh auth status >/dev/null 2>&1 || { echo "❌ gh no está autenticado. Ejecuta: gh auth login"; exit 1; }
	$(eval TS := $(shell date +%Y%m%d%H%M))
	$(eval NAME ?= LAIA-Whitepapers)
	$(eval TAG := $(TS)-$(NAME))
	$(eval TITLE := $(subst -,$(space),$(NAME)))
	$(eval DOC_ZIP := $(OUT_DIR)/documentos-$(TS).zip)
	$(eval WP_ZIP := $(OUT_DIR)/whitepapers-$(TS).zip)
	@echo "▶ Empaquetando documentos y whitepapers..."
	@cd "$(REPO_ROOT)" && zip -j "$(DOC_ZIP)" *.md
	@cd "$(REPO_ROOT)" && zip -j "$(WP_ZIP)" whitepapers/*.md
	@echo "▶ Creando release $(TAG)..."
	@gh release create "$(TAG)" "$(DOC_ZIP)" "$(WP_ZIP)" $(OUT_DIR)/*.pdf --title "$(TITLE)" --notes "Documentos y whitepapers de LAIA — $(TS)"
	@echo "✅ Release $(TAG) creado con documentos, whitepapers y PDFs."
