# Registro de uso de IA — apoio ao preenchimento da declaração

**Nome:** Brenda Luana Correia Bezerra

**Datas dos usos registrados:** 27/10/2026 e 02/11/2026

**Repositório:** https://github.com/Brendalu2005/AVD-20262-pratica-streamlit

## Como ler este registro

Os pedidos abaixo são **resumos das solicitações reais, agrupados por finalidade**,
não transcrições literais nem novos prompts apresentados como históricos.
Não são uma cópia completa das conversas. O registro descreve as contribuições
por etapa. A ausência de marcação não identifica, por si só, a autoria de um trecho.

Este Markdown não substitui o formulário individual da disciplina, a reflexão
pessoal, a assinatura ou a entrega de `prompts/DECLARACAO_IA.pdf` no repositório
e no Classroom. A opção de registro por blocos deve ser completada no formulário
com os usos relevantes; a alternativa de conversas completas exige os links
ou arquivos correspondentes.

## Ferramenta e skill utilizadas

- **Ferramenta:** Codex, da OpenAI, no ambiente de desenvolvimento. Modelo exato
  e plano não foram confirmados para todos os usos; não foram presumidos.
- **Skill oficial do Streamlit: utilizada.** A revisão consultou
  `developing-with-streamlit` e as referências da instalação local para
  layouts, temas, widgets e testes. Não se trata de uma ferramenta de IA
  independente, mas de instruções e documentação usadas pelo Codex.
- **Outros apoios técnicos:** na conferência do formulário, a skill de PDF
  orientou a leitura e inspeção das cinco páginas do documento.

## Participação da autoria registrada na conversa

- Trouxe ao projeto o dataset Spotify e o notebook pessoal de EDA já existente.
- Forneceu o roteiro, o guia `ALTAIR-CROSSFILTER.md`, as referências de layout
  e o modelo formal de declaração para orientar e conferir o trabalho.
- Solicitou implementações e revisões, estabelecendo limites como apresentar
  o resultado para aprovação e não realizar o deploy naquela etapa.
- Aprovou a revisão anterior e posteriormente autorizou ajustes documentais.
- Identificou o problema do limite de artistas e confirmou que queria analisar
  até 50 artistas em todos os gráficos e indicadores.

Essas ações demonstram direcionamento e revisão pela autoria. A conversa não
permite quantificar uma porcentagem de trabalho humano nem afirmar compreensão
individual de cada trecho, realização de todos os testes pela autoria ou
escolha exclusivamente humana das métricas.

## Usos registrados

### 1. Orientação sobre Git — 27/10/2026

- **Parte:** fluxo de trabalho do repositório.
- **Pedido, em resumo:** entender como integrar alterações remotas sem perder o trabalho local.
- **Contribuição da IA:** explicação de fetch, merge, resolução de conflitos e recuperação com abort, conforme o registro anterior.
- **Aproveitamento e decisões:** orientação para a autoria; não há registro de merge executado pela IA naquela etapa.
- **Verificação:** consulta do estado local; não se atribui à autoria uma execução não confirmada.

### 2. Implementação dos dashboards — 27/10/2026

- **Parte:** `app.py`, `app_spotify.py`, `src/`, tema, wireframe do Dashboard 2, justificativas e testes.
- **Pedido, em resumo:** auxiliar a implementar os requisitos da aula, incluindo gráficos, cache, abas, KPIs, seleção vinculada e documentação.
- **Contribuição da IA:** produção e adaptação de código para as colunas do Spotify, implementação da interação Altair/Streamlit, geração de wireframe, redação de documentação e testes automatizados.
- **Aproveitamento e decisões:** o resultado foi incorporado ao projeto e submetido a revisão. Houve sugestões de métricas e redação das justificativas pela IA; não se registra esse apoio como apenas sintático ou exclusivamente consultivo.
- **Verificação:** o registro anterior informa seis testes aprovados com unittest e AppTest em 27/10/2026.

### 3. Conferência e correções antes do deploy — 02/11/2026

- **Parte:** roteiro, notebooks, dados tratados, dashboards, rascunhos e documentação.
- **Pedido, em resumo:** identificar pendências, conferir coerência com o roteiro e corrigir o que faltava antes da publicação, apresentando o resultado para aprovação.
- **Contribuição da IA:** revisão do projeto; correção da exportação para o Spotify; validação do CSV; alinhamento das cores ao tema escuro/verde existente; revisão dos wireframes e atualização dos testes e documentos.
- **Aproveitamento e decisões:** a autoria aprovou a revisão. A EDA pessoal foi preservada. A proposta visual inicial foi mantida como histórico. O commit `24c19e0` registra essa revisão anterior, não todas as alterações posteriores.
- **Verificação:** os testes automatizados foram executados pela IA; os valores das 14 colunas mantidas foram comparados aos do CSV anterior, sem diferenças nas 500 linhas. Posteriormente, em 02/11/2026, a autoria confirmou nesta conversa que realizou todos os itens da conferência visual no navegador e que tudo funciona corretamente.

### 4. Discussão sobre métricas e gráficos — 02/11/2026

- **Parte:** adequação e limites dos indicadores e visuais existentes.
- **Pedido, em resumo:** avaliar se as métricas e gráficos utilizados eram adequados ao dashboard.
- **Contribuição da IA:** explicação das perguntas atendidas e dos limites de soma, mediana, Top 5, correlação, distribuição e comparação entre gêneros.
- **Aproveitamento e decisões:** não foi registrada nessa discussão uma substituição de métricas ou gráficos. A escolha acadêmica e a validação individual precisam ser confirmadas pela autoria.
- **Verificação:** análise conceitual dos indicadores implementados; não equivale a uma justificativa pessoal escrita pela estudante.

### 5. Melhoria do limite de artistas — 02/11/2026

- **Parte:** sidebar, preparação do recorte, ranking, testes e wireframes.
- **Pedido, em resumo:** corrigir o comportamento que mantinha dez artistas no ranking e fazia apenas um gráfico responder ao controle de quantidade.
- **Contribuição da autoria:** relatou o comportamento e confirmou o requisito de até 50 artistas em todos os gráficos e indicadores.
- **Contribuição da IA:** implementação do limite opcional compartilhado, seleção dos maiores volumes dentro dos filtros, ranking completo com rolagem e ajuda para distinguir quantidade de artistas de classes do histograma.
- **Aproveitamento e decisões:** o comportamento foi implementado conforme o requisito confirmado. As fórmulas dos KPIs foram mantidas, passando a responder ao novo recorte.
- **Verificação:** doze testes aprovados, incluindo limites de 50 e 100 artistas, comparação dos dados dos cinco gráficos, recorte vazio, poucos artistas e limite de um artista.

### 6. Formulário e marcações de IA — 02/11/2026

- **Parte:** modelo PDF de declaração, código e registros de uso.
- **Pedido, em resumo:** comparar o projeto com as exigências do formulário e acrescentar marcações de apoio de IA no código.
- **Contribuição da IA:** leitura do formulário, identificação das pendências e inclusão de comentários `[IA]` em blocos de gráficos, seleção vinculada, correlação, KPIs, validação e testes de integração.
- **Aproveitamento e decisões:** comentários adicionados aos blocos complexos. As marcações permanecem parciais e não cobrem todos os trechos com apoio de IA exigidos pelo formulário.
- **Verificação:** conferência dos comentários e do diff, sem mudança funcional nessa etapa.

### 7. Auditoria e atualização documental — 02/11/2026

- **Parte:** READMEs, justificativa, validação, prompts e registros de aprovação.
- **Pedido, em resumo:** conferir o atendimento ao roteiro e aos rascunhos, apresentar pendências antes de implementar e, após autorização, atualizar os registros com resumos dos pedidos.
- **Contribuição da IA:** conferência dos arquivos e execução dos doze testes; correção de instruções antigas da UCI; registro das aprovações e separação entre alterações anteriores já commitadas e mudanças locais posteriores.
- **Aproveitamento e decisões:** a autoria autorizou os ajustes. Os pedidos foram resumidos, sem inventar falas nem reduzir a contribuição documentada da IA a simples aconselhamento.
- **Verificação:** conferência documental e `git diff --check`. Não houve nova execução dos testes por mudanças somente textuais.

## Rascunhos e autoria das decisões analíticas

Os wireframes atuais de 02/11/2026 documentam revisões posteriores à implementação.
Isso está identificado nas imagens; não são apresentados como comprovação de
planejamento anterior. A proposta inicial foi preservada em
`entregas/proposta-inicial-spotify.png`.

A IA participou da proposta e da redação das justificativas das métricas. O
formulário da disciplina restringe esse tipo de uso. A aprovação da implementação
não altera esse histórico nem substitui a escolha e explicação individual.
A autoria deve esclarecer com a professora como regularizar os itens afetados,
sem substituir o histórico por uma descrição de apoio apenas consultivo.

## Situação e complementação individual

- Revisão anterior aprovada; ajustes dos filtros solicitados e confirmados; atualização documental autorizada.
- Marcações nos blocos complexos mantidas.
- Versão preparada para deploy registrada em `788f1c9`; o título foi ajustado em `c0741e3` e o link público incluído em `072f07f`.
- Conferência visual local realizada e aprovada pela autoria, conforme confirmação nesta conversa em 02/11/2026. Deploy informado como concluído pela autora; teste funcional completo do link público ainda não registrado.
- Formulário PDF assinado ainda não entregue no repositório. Turma, e-mail, data de entrega, reflexão de 8 a 15 linhas e assinatura precisam ser conferidos ou completados pela autoria.
- Nenhuma reflexão individual, assinatura ou declaração de compreensão do código foi produzida em nome da estudante.
