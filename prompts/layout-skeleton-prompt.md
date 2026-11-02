# Rascunhos → estrutura do app — versão revisada

Esta versão foi alinhada à revisão de 02/11/2026. Não é transcrição do prompt
original: o histórico de uso está em `declaracao-uso-ia.md`.

## Contexto

Sou estudante de Análise e Visualização de Dados. Quero explorar a audiência
acumulada dos artistas do dataset Spotify, com duas abas conforme `ROTEIRO.md`.

## Entrada

Anexe `entregas/rascunho-dashboard1.png` e `entregas/rascunho-dashboard2.png`.
Carregue `data/clean/dataset.csv` por `src/data_loader.py`.

Colunas: `Artist Name`, `Primary Genre`, `Artist Type`, `Debut Year`,
`Total Streams (in millions)`, `Lead Streams (in millions)`,
`Feature Streams (in millions)`, `Solo Streams (in millions)` e
`Collaborative Streams (in millions)`.

- Sidebar: gêneros e tipos por multisseleção; intervalo do ano de estreia.
- Dashboard 1: seleção de variáveis, intervalos numéricos, Pearson/Spearman,
  heatmap de correlação e histograma com escolha de variável/classes e cor por gênero.
- Dashboard 2: slider do tamanho do ranking na aba, contagem de artistas,
  soma atribuída, mediana de streams e participação do Top 5; barras de gênero
  com seleção vinculada aos KPIs, ranking e dispersão principal × participação.

## Restrições

Use Streamlit, Pandas e Altair, com `st.tabs`, `st.metric` e `st.cache_data`.
Preserve o tema escuro/verde de `.streamlit/config.toml`; use componentes nativos.
Não invente colunas nem dados. O ano é de estreia, não período de reproduções.
A soma de volumes atribuídos não representa streams únicos da plataforma.
Os intervalos numéricos da aba 1 não devem restringir a aba 2.
Trate seleção vazia, apenas uma variável, recorte vazio e correlação indefinida.
Siga `ALTAIR-CROSSFILTER.md` para a seleção gráfica da aba 2.

## Formato de saída

Código funcional de `app.py`, preservando os módulos `src/`, com eventuais
alterações justificadas. Documente fórmulas e limites em
`entregas/justificativa-metricas.md` e valide com os testes existentes.
Apresente a versão para aprovação antes de commit/push; não faça deploy.
