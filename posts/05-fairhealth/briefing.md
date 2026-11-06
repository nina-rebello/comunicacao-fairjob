# Post 05 · fairhealth (apresentação profunda da marca)

Mesma sequência do post 04 (fairdata): 5 slides, LinkedIn em PDF, convite
tradicional (sem pedir comentário), pouco texto, uma ideia por slide.

## Identidade visual

O template e a tipografia são os do post 04 (fairdata): Inter 800 nos títulos,
rótulo em caixa alta, slides claros e escuros alternados, grade de caixas,
lista numerada, conclusão em Instrument Serif itálico, botão em pílula e tags
de vidro na capa. Muda só a identidade, tirada do site (variáveis
`--health-*` da página da fairhealth, 06/11/2026):
- claro: menta `#E6F4F1` (no lugar do creme da FairJob);
- escuro: `#0E2521`, o verde quase preto dos títulos do site;
- destaque: verde-água `#00A895` (no escuro, `#2CC7B2` para contraste);
  texto secundário `#527A74`, como no site;
- capa: sem imagem (decisão de 06/11). As tags de vidro de quem atende no
  Escritório do Cuidado descem em diagonal, como a cascata da fairdata.

## O que o site diz (e o que entrou no carrossel)

- **Topo:** "Medicina preventiva in company". "Plano de saúde fica mais caro.
  Colaboradores ausentes. De novo." "O problema não é o plano. É como a
  empresa recebe o colaborador e, na sequência, como se lida com o
  diagnóstico." → capa e slide 2.
- **Número:** "70% dos custos do plano de saúde corporativo vêm de doenças
  crônicas evitáveis" (Revista de Saúde Pública da USP). Hipertensão,
  diabetes tipo 2, obesidade, burnout; aparecem primeiro na sinistralidade,
  antes do afastamento. → slide 2.
- **Escritório do Cuidado:** "O que é importante para você hoje?". Espaço
  físico de atendimento médico e psicológico dentro da empresa; "a
  proximidade aumenta a adesão. A adesão gera resultado." Atendimento
  preventivo; plantões alternados (médicos, psicólogos, assistentes sociais e
  felicitologistas); anamnese e medições com tecnologia; MEV; complementar ao
  plano e ao SST/SESMT; dados anonimizados para o RH no painel fairdata.
  → capa e slide 3.
- **MEV, 7 pilares:** alimentação, movimento, estresse, sono, vícios,
  relacionamentos, espiritualidade. Letramento contínuo e workshops.
- **Jornada de 12 meses:** mês 1 diagnóstico integrado (fairdata); meses 1 a
  12 Escritório do Cuidado (Plano Individual do Cuidado) e Programa MEV
  (letramento, fairedu integrado); mês 12 mensuração, relatório de impacto em
  sinistralidade para o CFO, preparação para a acreditação fairtrust.
  → slide 4.
- **NR-1:** Escritório do Cuidado e Programa MEV dão estrutura para as
  exigências da NR-1, "com registros e rastreabilidade". → slide 3, de leve.
- **Convite do site:** "Quanto custa não cuidar da saúde dos seus
  colaboradores?" Diagnóstico gratuito de 60 minutos para identificar os
  principais ofensores e dimensionar a operação de cuidado. → slide 5.

## Fora do carrossel de propósito

- Os números de estudos do site (−27% absenteísmo, +40% participação,
  R$2,7 por R$1, 12 meses, −26% custos médicos, "7h de sono = −33% burnout")
  e as frases "clinicamente comprovada em reverter" e "redução mensurável" de
  sinistralidade. São promessa clínica ou de resultado: pela voice.md, passam
  antes pela coordenação médica (CFM).
- "Sinistralidade acima de 75% encarece o plano" e "ROI apresentável ao board
  em 12 meses": promessa comercial.

## Antes de publicar

- [ ] Dr. Ronald aprova a menção médica (guia de carrossel, regra do CFM).
- [ ] Conferir a fonte do 70% (Revista de Saúde Pública da USP: artigo e
      ano). Se não achar, trocar o slide 2 por texto sem número.
- [ ] Confirmar se "felicitologista" pode aparecer como função na capa.

## Versão editável para o Canva

`carrossel-5-canva.pptx`: cada parágrafo é uma caixa de texto (com as cores,
pesos e itálicos de cada trecho) e cada caixa, linha, botão e tag é uma forma
nativa. As tags de vidro viram pílulas lisas, porque desfoque e sombra não
viram forma editável. Já importado no Canva (06/11): design DAHaKP9DUhI,
https://www.canva.com/d/C82HscEjr7uvne8. Depois da importação, os textos
receberam negrito pelo Canva e as caixas do slide 3 ganharam fundo
`#F2FAF8` e borda `#B3CCC7` para aparecer. Para regerar depois de mudar o
`carrossel-5.html`:

    node posts/05-fairhealth/canva/extrair.js
    python3 posts/05-fairhealth/canva/montar-pptx.py
