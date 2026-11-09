"""Converte o carrossel exportado do Canva (1080x1350) para post quadrado do LinkedIn (1080x1080).

Reduz cada slide para 80% (1350 * 0.8 = 1080) e centraliza na horizontal (sobra 108 px de cada
lado, no fundo do próprio slide). Posições, tamanhos, fontes, entrelinhas, espaçamento entre letras
e contornos são escalados juntos, então o layout fica igual, só menor.

Uso: python3 posts/05-fairhealth/canva/quadrado.py entrada.pptx saida.pptx
"""
import sys

from pptx import Presentation

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
PX = 9525
ESCALA = 0.8
MARGEM_X = int(108 * PX)


def escalar_xfrm(xfrm, deslocar):
    off, ext = xfrm.find(A + "off"), xfrm.find(A + "ext")
    if off is not None:
        x, y = int(off.get("x")), int(off.get("y"))
        off.set("x", str(int(x * ESCALA) + (MARGEM_X if deslocar else 0)))
        off.set("y", str(int(y * ESCALA)))
    if ext is not None:
        ext.set("cx", str(int(int(ext.get("cx")) * ESCALA)))
        ext.set("cy", str(int(int(ext.get("cy")) * ESCALA)))


def escalar_texto_e_linhas(el):
    for tag in ("rPr", "defRPr", "endParaRPr"):
        for r in el.iter(A + tag):
            for attr in ("sz", "spc"):
                if r.get(attr) is not None:
                    r.set(attr, str(int(round(int(r.get(attr)) * ESCALA))))
    for sp in el.iter(A + "spcPts"):
        sp.set("val", str(int(round(int(sp.get("val")) * ESCALA))))
    for ln in el.iter(A + "ln"):
        if ln.get("w") is not None:
            ln.set("w", str(int(int(ln.get("w")) * ESCALA)))
    for body in el.iter(A + "bodyPr"):
        for attr in ("lIns", "tIns", "rIns", "bIns"):
            if body.get(attr) is not None:
                body.set(attr, str(int(int(body.get(attr)) * ESCALA)))


def main(entrada, saida):
    prs = Presentation(entrada)
    prs.slide_height = prs.slide_width  # 1080 x 1080
    for slide in prs.slides:
        arvore = slide._element.find(f"{P}cSld/{P}spTree")
        for filho in arvore:
            # só as formas de primeiro nível: dentro de grupos, as filhas acompanham o grupo
            xfrm = filho.find(f"{P}spPr/{A}xfrm")
            if xfrm is None:
                xfrm = filho.find(f"{P}grpSpPr/{A}xfrm")
            if xfrm is None:
                xfrm = filho.find(f"{P}xfrm")
            if xfrm is not None:
                escalar_xfrm(xfrm, deslocar=True)
        escalar_texto_e_linhas(arvore)
    prs.save(saida)
    print("salvo:", saida, prs.slide_width // PX, "x", prs.slide_height // PX)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
