# Registro de uso de IA — apoio ao preenchimento da declaração

**Nome:** Brenda Luana Correia Bezerra

**Datas dos usos registrados:** 27/10/2026 e 02/11/2026

**Repositório:** https://github.com/Brendalu2005/AVD-20262-pratica-streamlit

## Como ler este registro

Reuni abaixo **resumos das minhas solicitações reais, agrupados por finalidade**.
Não os apresento como transcrições literais nem como uma cópia completa das
conversas. Registro as contribuições por etapa. A ausência de marcação não
identifica, por si só, a autoria de um trecho.

Uso este Markdown como apoio ao preenchimento do formulário individual da
disciplina. Ainda preciso completar a reflexão pessoal, assinar e entregar
`prompts/DECLARACAO_IA.pdf` no repositório e no Classroom. Devo completar os
blocos do formulário com os usos relevantes ou anexar as conversas completas,
conforme a opção de registro escolhida.

## Ferramenta e skill utilizadas

- **Ferramenta:** utilizei o Codex, da OpenAI, no ambiente de desenvolvimento.
  Não tenho confirmação do modelo exato e do plano de todos os usos registrados.
- **Skill oficial do Streamlit:** utilizei o apoio do Codex com a skill
  `developing-with-streamlit` e as referências locais de layouts, temas,
  widgets e testes. A skill reúne instruções e documentação; não é uma
  ferramenta de IA independente.
- **Outros apoios técnicos:** solicitei a conferência do formulário PDF;
  o Codex utilizou a skill de PDF para ler e inspecionar suas cinco páginas.

## Minha participação no projeto

- Trouxe ao projeto o dataset Spotify e meu notebook de EDA já existente.
- Forneci o roteiro, o guia `ALTAIR-CROSSFILTER.md`, as referências de layout
  e o modelo formal de declaração para orientar e conferir o trabalho.
- Solicitei implementações e revisões, pedindo a apresentação dos resultados
  para minha aprovação e a realização do deploy em uma etapa posterior.
- Aprovei a revisão anterior e posteriormente autorizei ajustes documentais.
- Identifiquei o problema do limite de artistas e confirmei que queria analisar
  até 50 artistas em todos os gráficos e indicadores.

Registro essas ações como parte do meu direcionamento e da minha revisão do
projeto. Não atribuo uma porcentagem de trabalho a cada participante nem
apresento os testes automatizados executados pelo Codex como execuções manuais
minhas. A escolha das métricas também recebeu contribuição de IA, descrita abaixo.

## Usos registrados

### 1. Orientação sobre Git — 27/10/2026

- **Parte:** fluxo de trabalho do repositório.
- **Pedido, em resumo:** entender como integrar alterações remotas sem perder o trabalho local.
- **Contribuição da IA:** explicação de fetch, merge, resolução de conflitos e recuperação com abort, conforme o registro anterior.
- **Aproveitamento e decisões:** recebi orientação sobre os comandos; não registro um merge executado pela IA naquela etapa.
- **Verificação:** solicitei a consulta do estado local e não declaro uma execução de merge não confirmada.

### 2. Implementação dos dashboards — 27/10/2026

- **Parte:** `app.py`, `app_spotify.py`, `src/`, tema, wireframe do Dashboard 2, justificativas e testes.
- **Pedido, em resumo:** auxiliar a implementar os requisitos da aula, incluindo gráficos, cache, abas, KPIs, seleção vinculada e documentação.
- **Contribuição da IA:** produção e adaptação de código para as colunas do Spotify, implementação da interação Altair/Streamlit, geração de wireframe, redação de documentação e testes automatizados.
- **Aproveitamento e decisões:** incorporei o resultado ao projeto para revisão. Recebi sugestões de métricas e redação de justificativas; não descrevo esse apoio como apenas sintático ou exclusivamente consultivo.
- **Verificação:** o registro anterior informa seis testes aprovados com unittest e AppTest em 27/10/2026.

### 3. Conferência e correções antes do deploy — 02/11/2026

- **Parte:** roteiro, notebooks, dados tratados, dashboards, rascunhos e documentação.
- **Pedido, em resumo:** identificar pendências, conferir coerência com o roteiro e corrigir o que faltava antes da publicação, apresentando o resultado para aprovação.
- **Contribuição da IA:** revisão do projeto; correção da exportação para o Spotify; validação do CSV; alinhamento das cores ao tema escuro/verde existente; revisão dos wireframes e atualização dos testes e documentos.
- **Aproveitamento e decisões:** aprovei a revisão, mantendo minha EDA e a proposta visual inicial como referências. O commit `24c19e0` registra essa revisão anterior, não todas as alterações posteriores.
- **Verificação:** recebi os resultados dos testes automatizados executados pelo Codex e da comparação das 14 colunas mantidas, sem diferenças nas 500 linhas. Em 02/11/2026, realizei a conferência visual no navegador e confirmei o funcionamento dos itens registrados.

### 4. Discussão sobre métricas e gráficos — 02/11/2026

- **Parte:** adequação e limites dos indicadores e visuais existentes.
- **Pedido, em resumo:** avaliar se as métricas e gráficos utilizados eram adequados ao dashboard.
- **Contribuição da IA:** explicação das perguntas atendidas e dos limites de soma, mediana, Top 5, correlação, distribuição e comparação entre gêneros.
- **Aproveitamento e decisões:** não solicitei nessa discussão a substituição de métricas ou gráficos. Ainda preciso explicitar minha escolha acadêmica e minha validação individual.
- **Verificação:** recebi uma análise conceitual dos indicadores implementados; não a apresento como uma justificativa pessoal escrita por mim.

### 5. Melhoria do limite de artistas — 02/11/2026

- **Parte:** sidebar, preparação do recorte, ranking, testes e wireframes.
- **Pedido, em resumo:** corrigir o comportamento que mantinha dez artistas no ranking e fazia apenas um gráfico responder ao controle de quantidade.
- **Minha contribuição:** relatei o comportamento e confirmei o requisito de até 50 artistas em todos os gráficos e indicadores.
- **Contribuição da IA:** implementação do limite opcional compartilhado, seleção dos maiores volumes dentro dos filtros, ranking completo com rolagem e ajuda para distinguir quantidade de artistas de classes do histograma.
- **Aproveitamento e decisões:** recebi a implementação conforme o requisito que confirmei, mantendo as fórmulas dos KPIs e aplicando o novo recorte.
- **Verificação:** doze testes aprovados, incluindo limites de 50 e 100 artistas, comparação dos dados dos cinco gráficos, recorte vazio, poucos artistas e limite de um artista.

### 6. Formulário e marcações de IA — 02/11/2026

- **Parte:** modelo PDF de declaração, código e registros de uso.
- **Pedido, em resumo:** comparar o projeto com as exigências do formulário e acrescentar marcações de apoio de IA no código.
- **Contribuição da IA:** leitura do formulário, identificação das pendências e inclusão de comentários `[IA]` em blocos de gráficos, seleção vinculada, correlação, KPIs, validação e testes de integração.
- **Aproveitamento e decisões:** mantive os comentários nos blocos complexos. Reconheço que as marcações são parciais e não cobrem todos os trechos com apoio de IA exigidos pelo formulário.
- **Verificação:** conferência dos comentários e do diff, sem mudança funcional nessa etapa.

### 7. Auditoria e atualização documental — 02/11/2026

- **Parte:** READMEs, justificativa, validação, prompts e registros de aprovação.
- **Pedido, em resumo:** conferir o atendimento ao roteiro e aos rascunhos, apresentar pendências antes de implementar e, após autorização, atualizar os registros com resumos dos pedidos.
- **Contribuição da IA:** conferência dos arquivos e execução dos doze testes; correção de instruções antigas da UCI; registro das aprovações e separação entre alterações anteriores já commitadas e mudanças locais posteriores.
- **Aproveitamento e decisões:** autorizei os ajustes e o registro resumido dos pedidos, sem apresentar resumos como falas literais nem descrever a contribuição da IA como simples aconselhamento.
- **Verificação:** conferência documental e `git diff --check`. Não houve nova execução dos testes por mudanças somente textuais.

## Rascunhos e autoria das decisões analíticas

Apresento os wireframes atuais de 02/11/2026 como revisões posteriores à
implementação, conforme a identificação nas imagens. Não os apresento como
comprovação de planejamento anterior. Mantenho a proposta inicial em
`entregas/proposta-inicial-spotify.png`.

Recebi apoio de IA na proposta e na redação das justificativas das métricas.
O formulário da disciplina restringe esse tipo de uso. Minha aprovação da
implementação não substitui minha escolha e explicação individual. Preciso
esclarecer com a professora como regularizar os itens afetados, mantendo o
registro do apoio efetivamente recebido.

## Situação e complementação individual

- Aprovei a revisão anterior, solicitei e confirmei os ajustes dos filtros e autorizei a atualização dos registros.
- Mantive as marcações nos blocos complexos.
- Versão preparada para deploy registrada em `788f1c9`; o título foi ajustado em `c0741e3` e o link público incluído em `072f07f`.
- Realizei a conferência visual local em 02/11/2026 e concluí o deploy. Ainda preciso registrar o teste funcional completo do link público.
- Ainda preciso entregar o formulário PDF assinado e conferir ou preencher turma, e-mail, data de entrega e minha reflexão de 8 a 15 linhas.
- Minha reflexão individual, assinatura e declaração de compreensão do código precisam ser preenchidas por mim.
