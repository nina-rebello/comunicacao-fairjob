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
  **Atualização 09/11:** o diagnóstico gratuito não existe mais; o texto foi
  removido do slide 5 (Instagram e LinkedIn) e das legendas.

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

## Versão de 6 slides (carrossel-6.html), com a apresentação comercial

Fonte nova: "fairhealth ppt planetree" (apresentação comercial, enviada em
06/11). O que entrou:
- **Prova (slide 5):** case Chemitec Agro-Veterinária, 01/01 a 07/07/2026:
  48 colaboradores atendidos (98% de adesão), 161 atendimentos, 81,3% de
  retorno para 2 ou mais atendimentos, 46 smartbands. Fonte: Relatório
  Escritório do Cuidado, Fairhealth × Chemitec.
- **Fechamento (slide 6):** "Cuidado é a nova inteligência organizacional."
  e "Medir · Cuidar · Conscientizar · Comprovar", com Cuidar em destaque.
- **Slide 3:** "Menos barreira. Mais adesão. Mais resultado." e "foco na
  causa raiz, não no sintoma".
- **Visual:** fundo claro `#F3FAF8` e escuro `#0F2A27` da apresentação,
  faixa curva do selo (`#94C6BD`) na capa, pílulas menta com texto verde,
  cards brancos com borda menta.

No Canva (06/11): design DAHaKP-yygY, https://www.canva.com/d/m5luPmjHqHO0EzS
(substitui o de 5 slides, DAHaKP9DUhI).

Fora de propósito: o case do Hospital Dia Santo Amaro (é do Escritório do
Paciente, não do Escritório do Cuidado em empresa) e os números de estudos
(−27% absenteísmo, R$2,7 por R$1 etc.), pela regra de promessa clínica.

- [ ] **Confirmar com a Chemitec** se o nome e os números podem sair em post
      público (a apresentação foi para um parceiro, não para o feed).

## Cores Tiffany (09/11)

Pedido: começar no Tiffany do slide 2 (a cor principal da marca) e intercalar
com o tom claro, sem mudar o conteúdo. Feito a partir do design editado pela
Nina (DAHaKP9DUhI), exportado do Canva (`canva/canva-exportado-0911.pptx`) e
recolorido por `canva/recolorir.py`:
- slides 1, 3 e 5 em Tiffany `#95C6BD`: título em `#F2FBF9`, destaque e
  rótulo em `#0F2A27`, botão em `#0F2A27`;
- slides 2 e 4 em menta `#E6F4F1`: título `#0E2521`, destaque `#00A895`.

Design novo no Canva: DAHabf-Y8GQ, https://www.canva.com/d/Ku7ChNWo-Jt03Az
(o DAHaKP9DUhI ficou como estava). Cards, pílulas e botão foram recriados
como formas nativas depois da importação, que os tinha trazido como imagem.

Versão final (09/11): o DAHabf-Y8GQ fica como está, com os ajustes da Nina
(texto escuro em `#23463F`, descrições do slide 4 com 71% de opacidade) e o
efeito de vidro nos cards do slide 3 e nas pílulas do slide 1.

## Versão LinkedIn quadrada 1080x1080 (09/11)

O redimensionamento automático do Canva estava sem cota, então a versão
quadrada foi montada a partir do export do DAHabf-Y8GQ
(`canva/canva-tiffany-0911.pptx`) por `canva/quadrado.py`: cada slide é reduzido
a 80% (1350 × 0,8 = 1080) e centralizado, com 108 px de fundo de cada lado.
Arquivo importado: `carrossel-5-linkedin-1080.pptx`.

Design no Canva: DAHabS3JyCs, https://www.canva.com/d/yHQT_JggkrV7BXW
(5 páginas de 1080x1080). Depois da importação, os textos foram reposicionados
nas posições do original × 0,8 (o export desloca o topo das caixas de texto), e
as pílulas e o halo do logo (slide 1), os cards de vidro (slide 3) e o botão
(slide 5) foram recriados como formas nativas, porque tinham vindo como imagem.

Atualização 09/11: a pedido da Nina, o efeito de vidro saiu dos dois designs
(Instagram e LinkedIn). Pílulas do slide 1 voltaram a menta `#F1FAF8` com borda
`#9ED9CF`, sem o halo atrás do logo; cards do slide 3 voltaram a brancos com
borda `#BFE3DC`, números e rótulos em `#00A895`.
