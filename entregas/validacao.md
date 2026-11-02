# Validação dos dashboards

Comando: `python -m unittest discover -s tests -v`.
Resultado em 02/11/2026: onze testes aprovados com unittest e Streamlit AppTest.

- Dashboard 1: seleção de zero, uma, duas e quatro variáveis; avisos adequados sem exceções.
- Distribuição: alternância de variável, quantidade de classes e distinção por gênero.
- Correlação: Pearson e Spearman; valor calculado no recorte confrontado com pandas, diferente da base completa; variáveis constantes resultam em tabela vazia, sem correlação inventada.
- Filtros: gêneros/tipos vazios, ano de estreia e intervalo numérico que deixa um único registro.
- KPIs: soma, mediana e proporção Top 5 comparadas com valores conhecidos; denominador zero e recorte vazio tratados.
- Seleção: função que aplica o payload do clique validada para nenhum, um e múltiplos gêneros.
- Ranking: alterar Top N não altera os KPIs do recorte.
- Entradas: `app.py` e `app_spotify.py` renderizam duas abas sem exceções.
- Integração da seleção: um evento de seleção Pop é injetado na chamada do gráfico; os quatro KPIs são confrontados com os valores esperados, e ranking/dispersão recebem somente artistas Pop.
- Independência: os intervalos numéricos da aba 1 não alteram os KPIs da aba 2.
- CSV incompatível: colunas ausentes e nomes de artista duplicados são rejeitados; o app apresenta aviso sem exceção não tratada.
- Exportação: o notebook é executado sobre uma fixture em pasta temporária; o CSV gerado é comparado ao esperado e o bruto permanece intacto. O teste não depende do CSV bruto ignorado pelo Git.

O AppTest valida execução e widgets, mas não simula o gesto de clique no canvas do Vega no navegador. O encadeamento usa o padrão do guia local: seleção nomeada por campo, `on_select="rerun"`, payload aplicado no Python e gráficos secundários construídos com os dados selecionados. Os dois rascunhos revisados foram inspecionados visualmente.

## Coerência antes do deploy

- Dashboard 1: sidebar compartilhada, controles na aba, correlação à esquerda e distribuição à direita; wireframe revisado corresponde à estrutura do código.
- Dashboard 2: controle Top N na aba, quatro KPIs, seleção por soma atribuída de gênero, ranking e dispersão; fórmulas e unidades correspondem à justificativa.
- Identidade: fundo escuro, destaque verde e fonte sem serifa; barras usam a cor do tema.
- Dados: exportação manual local do Spotify executada nesta revisão; 500 artistas, 14 colunas, sem ausentes numéricos. Mantém os volumes originais, sem variáveis experimentais de carreira nem logs na fonte do app.
- Comparação com o CSV do último commit: 500 linhas em ambas as versões e nenhuma diferença nas células das 14 colunas preservadas.
- EDA original e notebook do professor preservados. Os rascunhos atuais são revisões posteriores à implementação, com essa condição declarada nos próprios arquivos.
- Dependências do app e dos módulos `src/` constam em `requirements.txt` (Streamlit, Pandas e Altair; SciPy suporta Spearman).
- CSV e tema já eram versionados. Os novos arquivos e as alterações desta revisão ainda precisam de aprovação, commit e push.

## Conferência visual pendente da autoria

O navegador automatizado não estava disponível nesta sessão. Antes de aprovar,
execute `streamlit run app.py` e confira:

1. As duas abas, textos, gráficos e tema escuro/verde na sua janela.
2. Clique em um gênero na aba 2: KPIs, ranking e dispersão mudam juntos.
3. Shift + clique combina gêneros; duplo clique limpa a seleção.
4. Após selecionar um gênero no gráfico, mudar a sidebar limpa a seleção anterior.

Deploy e testes do link público não foram realizados, conforme solicitado.
