#!/usr/bin/env python3
"""Genera un pedido para Pixelido a partir de una lista de proyectos.

Uso: pedido_pixelido.py pedido.json salida.md
pedido.json: {"titulo": "...", "videos": [{"dir": "CANALES/...", "canal": "...",
  "tema": "...", "estilo": "...", "observaciones": ["..."], "pantalla_final": "..."}]}
"""
import json, re, sys
from pathlib import Path

def tabla_visual(guion):
    m = re.search(r"## 2\. INDICACIONES VISUALES.*?\n(\|.*?)(?:\n\n|\n## )", guion, re.S)
    return m.group(1).strip() if m else "[PENDIENTE: sin tabla de bloques]"

def miniatura(tym):
    texto = re.search(r"\*\*TEXTO DE LA MINIATURA:\*\*\s*(.+)", tym)
    prompt = re.search(r"\*\*PROMPT PARA GEMINI.*?\*\*\s*\n(.+)", tym)
    titulo = re.search(r"\*\*TÍTULO \(copiar tal cual\):\*\*\s*\n(.+)", tym)
    return (titulo.group(1).strip() if titulo else "[PENDIENTE]",
            texto.group(1).strip() if texto else "[PENDIENTE]",
            prompt.group(1).strip() if prompt else "[PENDIENTE]")

def main(spec, out):
    p = json.loads(Path(spec).read_text())
    o = [f"# {p['titulo']}", "", "Fases: 1 guion → 2 edición → 3 miniatura. Cada fase necesita la aprobación de Christian antes de pasar a la siguiente.", ""]
    o.append("## Índice")
    for i, v in enumerate(p["videos"], 1):
        o.append(f"{i}. {v['canal']} — {v['tema']}" + (f" — Guion: {v['drive']}" if v.get("drive") else ""))
    for i, v in enumerate(p["videos"], 1):
        d = Path(v["dir"])
        loc = (d / "LOCUCION_EDITOR.txt").read_text().strip()
        titulo, texto, prompt = miniatura((d / "TITULOS_Y_MINIATURAS.md").read_text())
        o += ["", "---", "", f"## VÍDEO {i} — {v['canal']}", "",
              f"**Título de publicación:** {titulo}", "",
              *( [f"**Guion en Google Drive:** {v['drive']}", ""] if v.get("drive") else [] ),
              "### Tema", v["tema"], "",
              f"### Guion ({len(loc.split())} palabras)", "", loc, "",
              "### Descripción de edición", v["estilo"], "",
              tabla_visual((d / "GUION.md").read_text()), "",
              "### Observaciones"] + [f"- {x}" for x in v["observaciones"]] + [
              f"- Pantalla final: {v['pantalla_final']}", "",
              "### Miniatura (fase 3)", f"- Texto exacto: **{texto}**",
              f"- Descripción visual: {prompt}"]
    Path(out).write_text("\n".join(o) + "\n")
    print(out, sum(len(x.split()) for x in o), "palabras")

if __name__ == "__main__":
    main(*sys.argv[1:3])
