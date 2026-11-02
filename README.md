# Spotify — análise de artistas e streams | AVD 2026.2

Projeto individual de **Brenda Luana Correia Bezerra**, desenvolvido na disciplina
Análise e Visualização de Dados da CESAR School a partir do
[repositório-modelo da disciplina](https://github.com/mfal-school/AVD-20262-pratica-streamlit).

**Aplicação publicada:** [Abrir o dashboard Spotify](https://brendalu2005-spotifystreamingperformance.streamlit.app/)

**Repositório:** [Brendalu2005/AVD-20262-pratica-streamlit](https://github.com/Brendalu2005/AVD-20262-pratica-streamlit)

## Preparação inicial

- Tema da EDA: **Spotify Streaming Performance Dataset**, com informações de artistas e volumes acumulados de streams.
- [EDA pessoal](notebooks/eda.ipynb): notebook preservado como referência da análise original.
- O notebook da professora permanece em `notebooks/arquivo-eda-original.ipynb`.
- Aula 21: preparação e exportação dos dados, estrutura do app, seletor de variáveis e sliders de intervalo.
- Aula 22: dois dashboards com Altair, filtros compartilhados, indicadores e seleção gráfica vinculada.
- Aula 23: ajustes finais e publicação no Streamlit Community Cloud.
- Os [rascunhos atuais](entregas/README.md) representam revisões posteriores à implementação; a proposta visual inicial foi preservada.

## Entrega da Aula 21

- `notebooks/eda.ipynb`: EDA pessoal.
- `notebooks/arquivo-eda-original.ipynb`: exemplo da professora para consulta.
- `notebooks/eda-com-downloads.ipynb`: preparação do Spotify com leitura local, validação e exportação do CSV tratado.
- `data/clean/dataset.csv`: base de consumo do app, com **500 artistas e 14 colunas**.
- [Rascunho do Dashboard 1](entregas/rascunho-dashboard1.png): sidebar, controles, correlação e distribuição.
- `app.py`: entrada principal, com seletor de variáveis e sliders de intervalo.
- [Template de prompt](prompts/layout-skeleton-prompt.md) e [registro de uso de IA](prompts/declaracao-uso-ia.md).

### Reproduzir os dados

Coloque o CSV original `Spotify Streaming Performance Dataset.csv` em
`data/raw/`. Execute todas as células de `notebooks/eda-com-downloads.ipynb`
a partir da raiz do projeto ou da pasta `notebooks/`. A última célula exporta
`data/clean/dataset.csv`. O bruto fica local, conforme o `.gitignore`, e não é
necessário para executar o app com o CSV tratado já versionado.

A preparação normaliza os nomes das colunas, converte campos numéricos,
trata valores inválidos e valida nomes preenchidos e uma linha por artista.
Os volumes permanecem na escala original, sem log nem capping. Colunas
experimentais da EDA, como `anos_carreira`, `streams_por_ano` e transformações
logarítmicas, não fazem parte da exportação usada pelo dashboard.

## Entrega da Aula 22

O **Dashboard 1 — Exploração** apresenta um mapa de calor de correlação
Pearson ou Spearman e um histograma da variável escolhida. A multisseleção
define as variáveis da análise; os sliders numéricos restringem somente essa
aba. O histograma permite ajustar o número máximo de classes e distinguir
artistas por gênero. Classes são agrupamentos, não quantidade de artistas.

Seleções de zero ou uma variável, recortes vazios, dados constantes e
correlações indefinidas recebem avisos específicos. Células com correlação
indefinida são omitidas do mapa. Correlação não implica causalidade.

A sidebar compartilha **gênero, tipo de artista, ano de estreia e limite opcional
de artistas** entre as duas abas. Ao ativar o limite e informar 50, por exemplo,
o app mantém até os 50 artistas com mais streams dentro dos demais filtros.
Desativar o limite restaura todos os disponíveis. Esse recorte não é uma amostra
aleatória; filtros adicionais podem deixá-lo com menos artistas que o teto informado.

A identidade visual usa fundo escuro, destaque verde e fonte sem serifa em
`.streamlit/config.toml`. O carregamento do CSV utiliza `@st.cache_data` com
validade de uma hora, e o cálculo da correlação também utiliza cache.

### Dashboard 2 — indicadores de audiência

O painel é voltado a estudantes e analistas de música e apresenta:

- Quantidade de artistas distintos no recorte.
- Soma dos streams atribuídos, em milhões.
- Mediana dos streams por artista, em milhões.
- Participação dos cinco maiores volumes no total do recorte, em percentual.

As fórmulas, justificativas e limitações estão em
[entregas/justificativa-metricas.md](entregas/justificativa-metricas.md).
O [rascunho do Dashboard 2](entregas/rascunho-dashboard2.png) documenta a estrutura atual.

Os três visuais são barras de streams atribuídos por gênero, ranking dos
artistas por streams e dispersão de streams como artista principal versus
participação. O ranking mostra todo o recorte com volume válido, com rolagem.

Clique em um gênero no primeiro gráfico para filtrar os quatro KPIs, o ranking
e a dispersão. Shift + clique combina gêneros; duplo clique limpa a seleção.
As barras por gênero mantêm o contexto do recorte compartilhado. Uma mudança
na população dos filtros reinicia a seleção gráfica.

O ano filtra a **estreia do artista**, não o período das reproduções. Os dados
não constituem uma série temporal. A soma dos volumes atribuídos pode contar
participações em duplicidade e não representa streams únicos do Spotify.
Recortes vazios mostram contagem zero e “Sem dados” nas métricas de streams.

### Verificações

```bash
python -m unittest discover -s tests -v
```

Na última execução registrada em 02/11/2026, **12 testes passaram**. Eles
verificam cálculos conhecidos dos KPIs, filtros, seleção de zero/uma/múltiplas
variáveis, correlação, recortes vazios, limites de 50 e 100 artistas,
integração do evento de seleção, validação do CSV e exportação do notebook.

A conferência visual local foi realizada e aprovada pela autora em 02/11/2026.
O registro está em [entregas/validacao.md](entregas/validacao.md). Os testes
locais são separados da conferência da aplicação publicada.

Para recriar os dois wireframes revisados:

```bash
python scripts/gerar_rascunho.py
```

## Entrega da Aula 23

A autora informou a publicação no Streamlit Community Cloud. O projeto utiliza
a branch `main` e o arquivo principal `app.py`; o CSV tratado e o tema estão
versionados. O link da aplicação aparece no início deste README.

- [Evidência da aplicação publicada](entregas/evidencia_app_publicado.jpg).
- [Checklist das entregas](entregas/README.md).
- [Registro de validação](entregas/validacao.md).
- [Registro de uso de IA](prompts/declaracao-uso-ia.md).

Ainda deve ser registrado o teste da URL pública em janela anônima, sem login,
com as duas abas, os filtros e a seleção gráfica. A captura publicada não
substitui essa conferência funcional.

A declaração formal de uso de IA preenchida e assinada permanece como
pendência de entrega, conforme [prompts/README.md](prompts/README.md).

### Dependências

`requirements.txt` reúne as dependências do app e de apoio aos notebooks,
com intervalos de versões. O ambiente local utilizado na validação é
**Python 3.14.5**. A última conferência com `pip check` não encontrou conflitos.

```bash
python -m pip install -r requirements.txt
```

O app lê apenas o CSV tratado versionado, por `src/data_loader.py`.
O CSV bruto é necessário somente para reproduzir a preparação dos dados.

### Registro de autoria e revisão

O projeto é individual. Os usos de IA e da skill oficial do Streamlit estão
registrados em [prompts/declaracao-uso-ia.md](prompts/declaracao-uso-ia.md).
Os comentários `[IA]` identificam os blocos complexos assinalados no código.
O registro em Markdown auxilia o preenchimento da declaração formal e não
substitui a reflexão individual nem a assinatura.

## Orientações do repositório-modelo

O passo a passo das Aulas 21, 22 e 23 está em [ROTEIRO.md](ROTEIRO.md).
Os dashboards se organizam em exploração quantitativa e indicadores de audiência.

## Setup

Use Python compatível com `requirements.txt`; o projeto foi validado localmente
com Python 3.14.5. Para criar e ativar o ambiente virtual:

| Sistema | Criar | Ativar |
| --- | --- | --- |
| macOS / Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |
| Windows (PowerShell) | `py -m venv .venv` | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `py -m venv .venv` | `.venv\Scripts\activate.bat` |

### Instalar e executar

Com o ambiente ativo, execute na raiz do projeto:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

A entrada alternativa `streamlit run app_spotify.py` abre a mesma implementação.

### Problemas comuns

- **Comando Python não encontrado:** no Windows, use `py` para criar o ambiente; no macOS/Linux, use `python3`. Depois, ative o ambiente virtual.
- **Streamlit ou biblioteca não encontrados:** ative o ambiente e instale `requirements.txt`.
- **CSV tratado não encontrado:** confira `data/clean/dataset.csv`. Para recriá-lo, coloque o bruto em `data/raw/` e execute o notebook de preparação.
- **CSV bruto não encontrado no notebook:** confirme o nome `Spotify Streaming Performance Dataset.csv` em `data/raw/`.

## Estrutura dos dados

| Pasta | Conteúdo | Versionada? |
| --- | --- | --- |
| `data/raw/` | CSV bruto para reproduzir a preparação | Apenas `.gitkeep` |
| `data/clean/` | CSV tratado consumido pelo app | Sim |

O app não depende de um caminho absoluto do computador. Não versione chaves,
tokens ou `.streamlit/secrets.toml`.

## IA neste projeto

As instruções oficiais do Streamlit podem ser instaladas no ambiente com:

```bash
streamlit skills --yes
```

As pastas locais de skills não são versionadas. O uso efetivo da skill e das
ferramentas está registrado em `prompts/`.

## Pasta `prompts/`

Guarda o [template de layout](prompts/layout-skeleton-prompt.md) e o
[registro de uso de IA](prompts/declaracao-uso-ia.md). Consulte
[prompts/README.md](prompts/README.md) para os requisitos da declaração formal.

## Pasta `entregas/`

Guarda os rascunhos dos dashboards, a justificativa das métricas, a evidência
da publicação e o registro de validação. Consulte o
[checklist das entregas](entregas/README.md).
