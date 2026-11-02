# AVD-20262-pratica-streamlit

Repositório utilizado para aula prática relacionada a Streamlit na disciplina Análise e Visualização de Dados da Cesar School no período de 2026.2.

Repositório-modelo das Aulas 21, 22 e 23: construção de dois dashboards em Streamlit a partir da EDA desenvolvida em sala. O deploy dos dashbords ocorrerá via Streamlit Community Cloud e serão os seguintes:

- Dashboard 1 = correlação + distribuição das variáveis quantitativas
- Dashboard 2 = KPIs

## Setup

Requer **Python 3.11 a 3.15**. Confira a sua versão antes de começar:

| Sistema | Verificar versão |
| --- | --- |
| macOS / Linux | `python3 --version` |
| Windows | `py --version` |

### 1. Criar e ativar o ambiente virtual

O nome do comando do Python muda por sistema (em muitas máquinas `python` nem existe). Use a linha do seu sistema:

| Sistema | Criar | Ativar |
| --- | --- | --- |
| macOS / Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |
| Windows (PowerShell) | `py -m venv .venv` | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `py -m venv .venv` | `.venv\Scripts\activate.bat` |

Se você tem várias versões instaladas, escolha uma compatível, por exemplo `python3.12 -m venv .venv` (macOS/Linux) ou `py -3.12 -m venv .venv` (Windows).

Com o ambiente ativo, o terminal mostra `(.venv)` no início da linha. **A partir daqui os comandos são iguais em todos os sistemas**, porque dentro do venv `python` e `pip` sempre existem.

### 2. Instalar, configurar a IA e rodar

```bash
python -m pip install -r requirements.txt

# Skills de IA do Streamlit (ver seção "IA neste projeto")
streamlit skills --yes

streamlit run app.py
```

### Problemas comuns

- **`python: command not found` / `python` não é reconhecido:** use `python3` (macOS/Linux) ou `py` (Windows) só para criar o venv; depois de ativado, `python` funciona.
- **Linux (Debian/Ubuntu): `ensurepip is not available` ou `No module named venv`:** instale `sudo apt install python3-venv` (ou `python3.X-venv` para a sua versão).
- **Windows: "a execução de scripts foi desabilitada" ao ativar no PowerShell:** rode uma vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, ou use o cmd.
- **Python fora de 3.11–3.15:** instale uma versão compatível em [python.org](https://www.python.org/downloads/) e crie o venv com ela, como no exemplo acima.
- **Apareceu `ModuleNotFoundError` ou `streamlit: command not found`:** o venv provavelmente não está ativo. Ative de novo e confira o `(.venv)` no prompt.
- **Erro de certificado no `pip install` (macOS, Python do python.org):** rode `Install Certificates.command`, na pasta Python 3.X em Aplicativos.
- **CSV do Spotify não encontrado:** coloque `Spotify Streaming Performance Dataset.csv` em `data/raw/` antes de executar `notebooks/eda-com-downloads.ipynb`. Esse notebook usa leitura local, sem download da UCI nem configuração de certificados.

## Estrutura de dados: `data/raw` vs `data/clean`

- `data/raw/`: o dataset **bruto**, como foi baixado. Nunca é editado à mão.
- `data/clean/`: o dataset **já tratado**, exportado na última célula do notebook de EDA (ex.: `df.to_csv("data/clean/dataset.csv", index=False)`). O `app.py` lê **somente** desta pasta, via `src/data_loader.py`.

### O que vai para o Git

| Pasta | Versionada? | Por quê |
| --- | --- | --- |
| `data/raw/` | **Não** (só o `.gitkeep`) | O bruto pode ser grande ou ter dados sensíveis, e o app não o usa. |
| `data/clean/` | **Sim** | O Streamlit Community Cloud faz deploy a partir do GitHub e só enxerga o que está no repositório. Sem o CSV tratado no repo, o app funciona na sua máquina e **quebra no deploy**. |

### Antes de dar `git push` com o dado tratado

- **O dado é público ou pode ser compartilhado?** Se não for claramente público, use um **repositório privado** (o Community Cloud permite conectar repositórios privados ao autorizar o GitHub; confirme na hora do deploy). Nesse caso, dê acesso de leitura ao professor (como colaborador ou pela organização).
- **Dado sensível** (nomes, CPF, e-mail, telefone, localização exata etc.): remova ou anonimize na EDA, antes de exportar para `data/clean/`. Isso vale mesmo em repositório privado.
- **Tamanho:** o GitHub rejeita arquivos acima de **100 MB**. Se o CSV tratado for grande, reduza colunas e linhas na EDA ou exporte em Parquet (`df.to_parquet(...)`, exige `pyarrow`).
- **Lembre de commitar o arquivo:** confira com `git status` que `data/clean/dataset.csv` aparece como novo arquivo.

## Passo a passo

### Implementação Spotify — Aula 22

Execute `streamlit run app.py` (a entrada `app_spotify.py` abre o mesmo app).
O app contém duas abas: exploração quantitativa com correlação Pearson/Spearman
e histogramas, e indicadores com seleção de gênero vinculada aos KPIs, ranking
e dispersão. Os filtros compartilhados são gênero, tipo, ano de estreia e
limite opcional de artistas. Ative “Limitar quantidade de artistas” na sidebar
e informe, por exemplo, 50 em “Máximo de artistas”: os dois dashboards passam
a usar até os 50 artistas com mais streams dentro dos demais filtros.
Desative o limite para usar todos os disponíveis. O ranking exibe o recorte
inteiro, com rolagem. “Número máximo de classes” controla somente os
agrupamentos do histograma, sem alterar a quantidade de artistas;
os intervalos numéricos do Dashboard 1 se aplicam somente à exploração.

O CSV contém volumes acumulados por artista, sem série temporal. Streams são
expressos em milhões; a soma dos volumes atribuídos não mede streams únicos.
Consulte [justificativa das métricas](entregas/justificativa-metricas.md),
[rascunho do Dashboard 1](entregas/rascunho-dashboard1.png),
[rascunho do Dashboard 2](entregas/rascunho-dashboard2.png) e
[guia de seleção](ALTAIR-CROSSFILTER.md).

Validação: `python -m unittest discover -s tests -v`.
Para recriar os dois wireframes revisados: `python scripts/gerar_rascunho.py`.
As imagens de 02/11/2026 são revisões posteriores à implementação.
A proposta visual inicial foi preservada em `entregas/proposta-inicial-spotify.png`.

1. `notebooks/eda.ipynb` contém a EDA pessoal preservada; `arquivo-eda-original.ipynb` mantém o exemplo do professor.
2. Para preparar os dados, coloque o CSV original `Spotify Streaming Performance Dataset.csv` em `data/raw/` e execute todas as células de `notebooks/eda-com-downloads.ipynb`. O download manual é a alternativa adotada conforme o roteiro.
3. O notebook exporta `data/clean/dataset.csv` com as colunas da fonte, nomes normalizados e validações, mantendo os volumes originais. Colunas experimentais/logs da EDA não são necessárias ao app.
4. Execute os testes e `streamlit run app.py` para revisar as duas abas.

**Estado em 02/11/2026:** a autoria aprovou a revisão anterior e autorizou os
ajustes de documentação após a conferência. O limite compartilhado de artistas
foi implementado conforme a confirmação da autoria. O commit `24c19e0` registra
a revisão anterior; as alterações locais posteriores ainda precisam de commit
e push. A autoria confirmou em 02/11/2026 que realizou a conferência visual
no navegador e que todos os itens funcionam corretamente. A declaração formal
assinada, a publicação e o teste do link público continuam pendentes.

## IA neste projeto

Este projeto usa o **streamlit skills**: um conjunto de instruções (arquivos `SKILL.md`) que a ferramenta de IA lê para escrever código Streamlit seguindo boas práticas (estrutura de layout, cache, widgets, etc.).

**Como instalar:** depois do `pip install -r requirements.txt`, rode na raiz do projeto:

```bash
streamlit skills        # interativo
streamlit skills --yes  # sem confirmações
```

O comando cria *symlinks* para as skills que acompanham a sua instalação do Streamlit, então elas se atualizam sozinhas quando você atualiza o pacote. (A opção `--global` instala para todos os projetos, em vez de só este.)

**Onde fica instalado:**

- `.claude/skills/`: lido pelo Claude Code.
- `.agents/skills/`: lido pelo Gemini CLI, que já encontra essa pasta sozinho.

Essas pastas **não são versionadas** (ver `.gitignore`): os symlinks apontam para o seu ambiente virtual e não funcionam em outra máquina. Cada pessoa roda `streamlit skills` no próprio clone.

**Se você usa outra ferramenta** (ChatGPT, Copilot Chat, etc.): abra o `SKILL.md` correspondente em `.agents/skills/` e cole o conteúdo manualmente no início do chat, antes do seu pedido.

O uso de IA deve ser declarado conforme a seção abaixo.

## Pasta `prompts/`

A pasta [prompts/](prompts/) guarda o template de prompt para transformar o rascunho de layout em esqueleto de código e a **Declaração de Uso de IA** exigida pelo Plano de Ensino. Veja [prompts/README.md](prompts/README.md).


## Aplicação publicada

[Acessar o dashboard Spotify](https://brendalu2005-spotifystreamingperformance.streamlit.app/)