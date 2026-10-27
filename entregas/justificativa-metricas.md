# Justificativa das métricas — Dashboard 2

## Planejamento antes da implementação

Público: estudantes e analistas de música interessados na distribuição da audiência. Fonte: `data/clean/dataset.csv`, uma fotografia de volumes acumulados por artista, sem série temporal de reproduções.

1. Variáveis: `Artist Name`, `Total Streams (in millions)`, `Primary Genre`, `Artist Type` e `Debut Year`. Streams são expressos em milhões.
2. Métricas: contagem de artistas, soma de streams atribuídos, mediana por artista e participação do Top 5 no recorte.
3. Widgets: multisseleção de gêneros e tipos, intervalo de estreia e tamanho do ranking (5–20). Categorias vazias significam nenhum artista. O ano filtra a estreia, não a data das reproduções. Clique em uma barra de gênero restringe KPIs, ranking e dispersão; Shift permite múltiplos gêneros e duplo clique limpa a seleção.
4. Layout: sidebar compartilhada; duas abas; no Dashboard 2, quatro KPIs, barras de gênero para seleção e ranking/dispersão abaixo. `rascunho-dashboard2.png` registra o planejamento antes do código do dashboard.

## Artistas no recorte

- **Variável e fórmula:** contagem de nomes distintos em `Artist Name`.
- **Teoria:** frequência absoluta, medida de volume.
- **Por que foi escolhida:** contextualiza o tamanho da população comparada.
- **O que comunica ao público:** quantos artistas atendem aos filtros e à seleção gráfica.
- **Decisão apoiada:** avaliar a abrangência do recorte antes de comparar segmentos.

## Streams atribuídos aos artistas

- **Variável e fórmula:** soma de `Total Streams (in millions)`, excluindo ausentes.
- **Teoria:** soma, medida de volume acumulado.
- **Por que foi escolhida:** dimensiona a audiência atribuída aos artistas selecionados.
- **O que comunica ao público:** magnitude acumulada do recorte, em milhões.
- **Decisão apoiada:** comparar o volume de segmentos usando a mesma fonte.
- **Limite:** participações podem atribuir a mesma reprodução a vários artistas; a soma não mede reproduções únicas do Spotify nem faturamento.

## Streams medianos por artista

- **Variável e fórmula:** mediana dos valores válidos de `Total Streams (in millions)`.
- **Teoria:** tendência central, menos sensível a superestrelas que a média.
- **Por que foi escolhida:** descreve o centro de uma distribuição assimétrica.
- **O que comunica ao público:** metade dos valores válidos fica abaixo ou igual à mediana, e metade acima ou igual.
- **Decisão apoiada:** comparar um artista com uma referência do seu segmento.

## Participação do Top 5

- **Variável e fórmula:** 100 × soma dos cinco maiores volumes / soma dos volumes válidos do recorte. Com menos de cinco artistas, usa todos os disponíveis. Denominador zero resulta em “Sem dados”.
- **Teoria:** proporção percentual, medida de concentração.
- **Por que foi escolhida:** revela quanto da audiência depende de poucos artistas.
- **O que comunica ao público:** concentração de volume entre as maiores audiências.
- **Decisão apoiada:** discutir diversidade e concentração no segmento. O tamanho do ranking não altera esta definição fixa de Top 5.

## Regras e limites comuns

Todos os KPIs respondem à sidebar e ao clique no gráfico de gêneros. Recortes vazios mostram contagem zero e “Sem dados” nas métricas de streams. O ranking não limita a população dos KPIs. Valores inválidos, infinitos ou negativos de streams são tratados como ausentes. Não se inferem causalidade, crescimento ou evolução temporal deste retrato. Categorias ausentes aparecem como “Não informado”.
