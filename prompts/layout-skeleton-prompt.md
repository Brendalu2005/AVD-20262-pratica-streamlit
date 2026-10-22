# Template: rascunho de layout → esqueleto do app

Preencha cada bloco e envie à ferramenta de IA.

## Contexto

<!-- Sou estudante de Ciência da Computação e estou desenvolvendo um dashboard interativo com Streamlit para analisar dados de streaming musical do Spotify. O objetivo é explorar o desempenho de artistas, comparar gêneros musicais e identificar padrões entre streams como artista principal e como participação em faixas. O dashboard deve facilitar a interpretação dos dados por meio de filtros, indicadores e visualizações interativas. -->

## Entrada

<!-- Utilize a imagem de rascunho anexada como referência visual para a estrutura da interface. A imagem representa a organização desejada para o dashboard .

Imagem de referência: prompts\prof_rascunho_dashboard1.png. 

Colunas relevantes do dataset:

- `Artist Name`: nome do artista.
- `Total Streams (in millions)`: total de streams, em milhões.
- `Lead Streams (in millions)`: streams como artista principal, em milhões.
- `Feature Streams (in millions)`: streams como participação em faixas, em milhões.
- `Primary Genre`: gênero musical principal.
- `Artist Type`: tipo de artista.
- `Debut Year`: ano de estreia.
- `anos_carreira`: anos de carreira, caso disponível.

Perguntas que o dashboard deve responder:

- Quais artistas possuem o maior número de streams?
- Qual é a quantidade de artistas e o total de streams no recorte selecionado?
- Qual artista apresenta a maior audiência em streams?
- Quais gêneros musicais possuem a maior média de streams por artista?
- Existe alguma relação entre os streams como artista principal e os streams como participação?

Descrição do layout desejado:

1. **Sidebar à esquerda:** filtros de gênero musical, tipo de artista, intervalo de ano de estreia e quantidade de artistas exibidos no ranking.
2. **Cabeçalho:** título "Spotify Streaming Performance" e uma breve descrição do dashboard.
3. **Indicadores no topo:** três cartões com a quantidade de artistas no recorte, o total de streams e o artista com maior audiência.
4. **Área central:** dois gráficos de barras lado a lado, um com o ranking dos artistas por streams e outro com a média de streams por gênero.
5. **Área inferior:** gráfico de dispersão comparando os streams como artista principal e como participação em faixas.
-->

## Restrições

<!-- Utilizar Python, Streamlit, Pandas e Plotly.

Manter o carregamento dos dados por meio da função load_data() do módulo src/data_loader.py.

Implementar os filtros na sidebar e aplicá-los antes de calcular os indicadores e construir os gráficos.

Utilizar os nomes das colunas existentes no dataset, sem inventar dados ou assumir colunas que não estejam disponíveis.

Preservar a lógica de tratamento numérico das colunas necessárias às análises.

Criar gráficos interativos com Plotly, incluindo informações adicionais nos detalhes exibidos ao passar o cursor sobre os elementos.

Utilizar uma identidade visual inspirada no rascunho: fundo claro, tons de laranja, textos em cinza-escuro e cartões com bordas arredondadas.

Organizar o layout de forma responsiva, aproveitando a largura disponível na página.

Não substituir o carregamento de dados por dados fictícios.

Não alterar desnecessariamente outros arquivos do projeto, especialmente src/data_loader.py.

Não adicionar gráficos ou funcionalidades que não tenham sido solicitados sem justificar sua necessidade. -->

## Formato de saída

<!-- Gere o código completo e funcional do arquivo app.py, pronto para ser integrado ao projeto existente.

Organize o código em seções claras:
- Configuração da página e cabeçalho.
- Carregamento e preparação dos dados.
- Configuração dos filtros.
- Aplicação dos filtros.
- Cálculo dos indicadores.
- Construção dos gráficos.
- Organização final do layout.
- Utilize comentários curtos para identificar as seções principais. Não implemente funcionalidades fictícias nem deixe partes essenciais como # TODO.

- Antes de apresentar o código, verifique se os nomes das colunas utilizados correspondem aos informados, se os filtros afetam todos os indicadores e gráficos e se o código é compatível com Streamlit e Plotly. Caso alguma coluna necessária não esteja disponível, informe a limitação em vez de inventar informações. -->
