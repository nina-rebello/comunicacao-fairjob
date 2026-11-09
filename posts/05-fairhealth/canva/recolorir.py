"""Troca as cores do carrossel da fairhealth exportado do Canva (PPTX), sem mexer no conteúdo.

Esquema pedido em 09/11: começa no Tiffany (as cores que a Nina definiu no slide 2) e intercala
com o tom claro. Slides 1, 3 e 5 em Tiffany; slides 2 e 4 em menta claro.

- Tiffany: fundo #95C6BD, rótulo e palavra em destaque em #0F2A27, título principal em #F2FBF9,
  texto corrido em #0F2A27, textos pequenos (@fairjob.br, assinatura) em #23463F.
- Claro: fundo #E6F4F1, rótulo e destaque em #00A895, título em #0E2521, texto corrido em #527A74.

Cards e pílulas (fundo claro próprio) ficam como estão.

Uso: python3 posts/05-fairhealth/canva/recolorir.py entrada.pptx saida.pptx
"""
import sys

from pptx import Presentation

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"

TIFFANY, MENTA = "95C6BD", "E6F4F1"
BRANCO, ESCURO, PEQUENO = "F2FBF9", "0F2A27", "23463F"
VERDE, TITULO_CLARO, TEXTO_CLARO, LINHA_CLARA, LINHA_TIFFANY = "00A895", "0E2521", "527A74", "C8D7D4", "C6E5DF"

# por slide: fundo, troca geral de cores, textos com cor própria (pelo começo do texto)
# e grupos/textos que ficam como estão (cards e pílulas)
REGRAS = {
    1: dict(fundo=TIFFANY,
            troca={"0E2521": BRANCO, "00A895": ESCURO, "527A74": PEQUENO},
            proteger_grupos={"Group 5", "Group 11", "Group 17", "Group 23"}),
    2: dict(fundo=MENTA,
            troca={"F2FBF9": TITULO_CLARO, "0F2A27": VERDE, "0E2521": TEXTO_CLARO,
                   "324B48": VERDE, "A8C7C1": TEXTO_CLARO},
            textos={"É como": {"0F2A27": TEXTO_CLARO}}),
    3: dict(fundo=TIFFANY,
            troca={"0F2A27": BRANCO, "00A895": ESCURO, "527A74": PEQUENO, "D3DCDA": LINHA_TIFFANY},
            proteger_grupos={"Group 2", "Group 4", "Group 6", "Group 8"},
            proteger_textos=("01", "02", "03", "04", "ATENDIMENTO", "EQUIPE", "ESTILO", "DADOS",
                             "Médico e", "Médicos,", "Foco na", "Anonimizados"),
            textos={"Por que dentro": {"00A895": BRANCO}, "Menos barreira": {"0F2A27": ESCURO}}),
    4: dict(fundo=MENTA,
            troca={"F2FBF9": TITULO_CLARO, "2CC7B2": VERDE, "A8C7C1": TEXTO_CLARO, "324B48": LINHA_CLARA}),
    5: dict(fundo=TIFFANY,
            troca={"0E2521": BRANCO, "00A895": ESCURO, "527A74": PEQUENO, "C8D7D4": LINHA_TIFFANY},
            textos={"Diagnóstico gratuito": {"527A74": ESCURO},
                    "fairhealth.com.br": {"0E2521": ESCURO}, "ola@fairjob": {"0E2521": ESCURO}}),
}


def trocar(elemento, mapa):
    for c in elemento.iter(A + "srgbClr"):
        nova = mapa.get(c.get("val", "").upper())
        if nova:
            c.set("val", nova)


def percorrer(shapes, regra, log):
    for sh in shapes:
        if sh.shape_type == 6:  # grupo
            if sh.name in regra.get("proteger_grupos", set()):
                continue
            percorrer(sh.shapes, regra, log)
            continue
        texto = sh.text_frame.text if sh.has_text_frame else ""
        if texto and texto.startswith(regra.get("proteger_textos", ())):
            continue
        mapa = dict(regra["troca"])
        for inicio, extra in regra.get("textos", {}).items():
            if texto.startswith(inicio):
                mapa.update(extra)
        antes = [c.get("val") for c in sh._element.iter(A + "srgbClr")]
        trocar(sh._element, mapa)
        depois = [c.get("val") for c in sh._element.iter(A + "srgbClr")]
        if antes != depois:
            log.append(f"  {sh.name:12} {texto[:32]!r:36} {antes} -> {depois}")


def main(entrada, saida):
    prs = Presentation(entrada)
    for n, slide in enumerate(prs.slides, 1):
        regra = REGRAS[n]
        bg = slide._element.find(f"{P}cSld/{P}bg")
        for c in bg.iter(A + "srgbClr"):
            c.set("val", regra["fundo"])
        log = []
        percorrer(slide.shapes, regra, log)
        print(f"slide {n}: fundo {regra['fundo']}")
        print("\n".join(log))
    prs.save(saida)
    print("salvo:", saida)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
