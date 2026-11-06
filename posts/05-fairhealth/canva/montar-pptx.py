"""Monta o carrossel da fairhealth como PPTX editável para o Canva.

Lê canva/slides.json (gerado por extrair.js a partir do carrossel-5.html) e recria cada slide
com elementos nativos: fundo, formas (caixas, linhas, botão, pílulas), imagens (logo e ícones)
e um bloco de texto por parágrafo, com as cores, pesos e itálicos de cada trecho.

Uso: python3 posts/05-fairhealth/canva/montar-pptx.py
"""
import json
import os
import re

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Emu, Pt

PASTA = os.path.dirname(os.path.abspath(__file__))
POST = os.path.dirname(PASTA)
PX = 9525  # EMU por pixel (96 dpi)


def emu(v):
    return Emu(int(round(v * PX)))


def rgba(css):
    n = [float(x) for x in re.findall(r"[\d.]+", css)]
    return n[0], n[1], n[2], (n[3] if len(n) > 3 else 1.0)


def cor(css, fundo=None):
    """Cor CSS em RGBColor; transparência é misturada com a cor de fundo do slide."""
    r, g, b, a = rgba(css)
    if a < 1 and fundo is not None:
        fr, fg, fb, _ = rgba(fundo)
        r, g, b = (r * a + fr * (1 - a), g * a + fg * (1 - a), b * a + fb * (1 - a))
    return RGBColor(int(round(r)), int(round(g)), int(round(b)))


def fonte(run):
    """Nome da fonte e negrito, pelo peso do CSS (o Canva lê o nome da família com o peso)."""
    familia = run["fonte"]
    if "Instrument Serif" in familia:
        return "Instrument Serif", False
    peso = int(run["peso"])
    if peso >= 800:
        return "Inter ExtraBold", False
    if peso >= 700:
        return "Inter", True
    if peso >= 600:
        return "Inter SemiBold", False
    if peso >= 500:
        return "Inter Medium", False
    return "Inter", False


def sem_sombra(shape):
    shape.shadow.inherit = False


def main():
    slides = json.load(open(os.path.join(PASTA, "slides.json")))
    prs = Presentation()
    prs.slide_width = emu(1080)
    prs.slide_height = emu(1350)
    vazio = prs.slide_layouts[6]

    for s in slides:
        slide = prs.slides.add_slide(vazio)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = cor(s["fundo"])

        for f in s["formas"]:
            tipo = MSO_SHAPE.ROUNDED_RECTANGLE if f["raio"] > 0.5 else MSO_SHAPE.RECTANGLE
            sh = slide.shapes.add_shape(tipo, emu(f["x"]), emu(f["y"]), emu(f["w"]), emu(f["h"]))
            if tipo == MSO_SHAPE.ROUNDED_RECTANGLE:
                sh.adjustments[0] = min(0.5, f["raio"] / min(f["w"], f["h"]))
            if f["fundo"]:
                sh.fill.solid()
                sh.fill.fore_color.rgb = cor(f["fundo"], s["fundo"])
            else:
                sh.fill.background()
            if f["borda"]:
                sh.line.color.rgb = cor(f["borda"]["c"], s["fundo"])
                sh.line.width = Pt(max(f["borda"]["w"], 1) * 0.75)
            else:
                sh.line.fill.background()
            sem_sombra(sh)

        for im in s["imagens"]:
            if im.get("icone") is not None:
                caminho = os.path.join(PASTA, f"icone-{im['icone']}.png")
            else:
                caminho = os.path.normpath(os.path.join(POST, im["src"]))
            slide.shapes.add_picture(caminho, emu(im["x"]), emu(im["y"]), emu(im["w"]), emu(im["h"]))

        for t in s["textos"]:
            lh = t["entrelinha"]
            ch = t["h"] - (t["linhas"] - 1) * lh  # altura da área de texto de uma linha
            topo = t["y"] - (lh - ch) / 2
            if t["linhas"] > 1:
                x, largura = t["x"], t["larguraBloco"] - (t["x"] - t["esquerdaBloco"]) + 2
            else:
                x, largura = t["x"], min(t["w"] * 1.08 + 10, 1080 - t["x"])
            caixa = slide.shapes.add_textbox(emu(x), emu(topo), emu(largura), emu(lh * t["linhas"]))
            tf = caixa.text_frame
            tf.word_wrap = True
            tf.auto_size = MSO_AUTO_SIZE.NONE
            tf.vertical_anchor = MSO_ANCHOR.TOP
            tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.line_spacing = Pt(lh * 0.75)
            p.alignment = {"center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT}.get(t["alinhamento"], PP_ALIGN.LEFT)
            for r in t["runs"]:
                run = p.add_run()
                run.text = r["txt"]
                nome, negrito = fonte(r)
                run.font.name = nome
                run.font.bold = negrito
                run.font.italic = r["italico"]
                run.font.size = Pt(r["tam"] * 0.75)
                run.font.color.rgb = cor(r["cor"], s["fundo"])
                if r["esp"]:
                    run.font._rPr.set("spc", str(int(round(r["esp"] * 0.75 * 100))))

    destino = os.path.join(POST, "carrossel-5-canva.pptx")
    prs.save(destino)
    print("salvo:", destino)


if __name__ == "__main__":
    main()
