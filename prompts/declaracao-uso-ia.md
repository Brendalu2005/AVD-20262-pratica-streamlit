# Declaração de Uso de IA

**Nome:** não informado nesta conversa; preencher com o nome da autoria acadêmica.
**Data:** 27/10/2026

## Ferramenta

Codex (OpenAI), no ambiente de desenvolvimento do projeto. Identificador exato do modelo não exposto nesta sessão.

## Prompt usado

### Conversa 1 — Git

> como fazer merge sem perder minhas alterações remotas?

A IA consultou o estado local e explicou `git fetch origin`, `git merge origin/main`, resolução de conflitos, `git merge --abort` e push normal. Não executou o merge nessa etapa.

### Conversa 2 — implementação da aula

Pedido registrado abaixo em texto normalizado (sem os escapes de Markdown enviados pelo editor):

> implemente os seguintes requisitos, se ainda não forem implementados:
>
> 1. Adicione os gráficos de verdade ao Dashboard 1, usando `@st.cache_data`. Seaborn é permitido, Plotly é uma opção interativa e Altair é preferível pela seleção vinculada entre gráficos. Consulte `ALTAIR-CROSSFILTER.md`.
> 2. Teste o Dashboard 1 com 0 variáveis, 1 variável, 2 ou mais e o recálculo de correlação/distribuição com combinações distintas de widgets. Ajuste o que quebrar.
> 3. Escolha fundo, cor de destaque e fonte em `.streamlit/config.toml`.
> 4. Estruture o Dashboard 2: selecione as variáveis dos KPIs; proponha métricas ligadas à Teoria de Métricas Básicas; defina os widgets antes de codar; só então desenhe o rascunho em `entregas/rascunho-dashboard2.jpg` ou `.png`.
> 5. Crie abas `st.tabs` separando os dashboards no mesmo app.
> 6. Implemente o Dashboard 2 a partir do rascunho: widgets, `st.metric` e visuais Altair. Ligue seleção gráfica às métricas e outros gráficos conforme o guia.
> 7. Documente a escolha das métricas e o que comunicam em `entregas/justificativa-metricas.md`.
> 8. Atualize `prompts/declaracao-uso-ia.md` com as conversas desta aula.
> 9. Commit + push.
>
> As entregas da aula devem ficar completas; implementação pendente pode terminar na Aula 23.

Complemento do usuário:

> adicionei ALTAIR-CROSSFILTER.md

A IA leu o guia adicionado e adaptou o exemplo de seleção por clique para `Primary Genre` no CSV do Spotify. Planejou e gerou o wireframe antes de implementar o Dashboard 2. Produziu código, documentação e testes automatizados com `unittest` e `AppTest`.

## O que foi aceito, modificado ou rejeitado e por quê

- **Implementado para revisão da autoria:** dois dashboards, gráficos Altair, cache, filtros, tema laranja, rascunho, justificativas e testes. A validação acadêmica final cabe à autoria; não houve declaração posterior de aceite de cada escolha.
- **Modificado pela IA no esqueleto:** colunas de doenças cardíacas substituídas pelas colunas reais do Spotify. `app_spotify.py` passou a abrir a mesma implementação de `app.py`, evitando dois apps divergentes.
- **Escolhas técnicas:** KPIs de volume, tendência central e concentração; seleção de gênero com `on_select="rerun"`; ano de estreia não apresentado como período de streams.
- **Rejeitado pelo usuário:** nenhuma rejeição explicitada nesta conversa.
