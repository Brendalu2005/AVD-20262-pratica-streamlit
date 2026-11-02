# Validação dos dashboards

Comando: `python -m unittest discover -s tests -v`.
Resultado em 02/11/2026: doze testes aprovados com unittest e Streamlit AppTest.

- Dashboard 1: seleção de zero, uma, duas e quatro variáveis; avisos adequados sem exceções.
- Distribuição: alternância de variável, quantidade de classes e distinção por gênero.
- Correlação: Pearson e Spearman; valor calculado no recorte confrontado com pandas, diferente da base completa; variáveis constantes resultam em tabela vazia, sem correlação inventada.
- Filtros: gêneros/tipos vazios, ano de estreia e intervalo numérico que deixa um único registro.
- KPIs: soma, mediana e proporção Top 5 comparadas com valores conhecidos; denominador zero e recorte vazio tratados.
- Seleção: função que aplica o payload do clique validada para nenhum, um e múltiplos gêneros.
- Limite compartilhado: informar 50 ou 100 artistas atualiza os KPIs; com 50, o teste compara os dados dos cinco gráficos ao mesmo conjunto esperado, incluindo o recálculo da correlação. Desativar o limite restaura toda a população disponível.
- Bordas do limite: filtros com menos artistas que o teto, categorias vazias e limite de um artista são tratados sem exceções, mantendo o número solicitado no controle.
- Entradas: `app.py` e `app_spotify.py` renderizam duas abas sem exceções.
- Integração da seleção: um evento de seleção Pop é injetado na chamada do gráfico; os quatro KPIs são confrontados com os valores esperados, e ranking/dispersão recebem somente artistas Pop.
- Independência: os intervalos numéricos da aba 1 não alteram os KPIs da aba 2.
- CSV incompatível: colunas ausentes e nomes de artista duplicados são rejeitados; o app apresenta aviso sem exceção não tratada.
- Exportação: o notebook é executado sobre uma fixture em pasta temporária; o CSV gerado é comparado ao esperado e o bruto permanece intacto. O teste não depende do CSV bruto ignorado pelo Git.

O AppTest valida execução e widgets, mas não simula o gesto de clique no canvas do Vega no navegador. O encadeamento usa o padrão do guia local: seleção nomeada por campo, `on_select="rerun"`, payload aplicado no Python e gráficos secundários construídos com os dados selecionados. Os dois rascunhos revisados foram inspecionados visualmente.

## Coerência antes do deploy

- Dashboard 1: sidebar compartilhada, controles na aba, correlação à esquerda e distribuição à direita; wireframe revisado corresponde à estrutura do código.
- Dashboard 2: quatro KPIs, seleção por soma atribuída de gênero, ranking com rolagem e dispersão. O limite opcional de artistas fica na sidebar e é compartilhado pelas duas abas; fórmulas e unidades correspondem à justificativa.
- Identidade: fundo escuro, destaque verde e fonte sem serifa; barras usam a cor do tema.
- Dados: exportação manual local do Spotify executada nesta revisão; 500 artistas, 14 colunas, sem ausentes numéricos. Mantém os volumes originais, sem variáveis experimentais de carreira nem logs na fonte do app.
- Comparação com o CSV do último commit: 500 linhas em ambas as versões e nenhuma diferença nas células das 14 colunas preservadas.
- EDA original e notebook do professor preservados. Os rascunhos atuais são revisões posteriores à implementação, com essa condição declarada nos próprios arquivos.
- Dependências do app e dos módulos `src/` constam em `requirements.txt` (Streamlit, Pandas e Altair; SciPy suporta Spearman).
- CSV, tema e rascunhos são versionados. A revisão anterior foi aprovada e registrada no commit `24c19e0`; os ajustes posteriores de filtros, marcações e documentação ainda estão locais e precisam de commit e push.

## Conferência visual concluída

Em 02/11/2026, foi realizado todos os itens da conferência visual e tudo está funcionando corretamente:

1. As duas abas, textos, gráficos e tema escuro/verde.
2. Seleção de gênero na aba 2, atualizando KPIs, ranking e dispersão.
3. Shift + clique para combinar gêneros e duplo clique para limpar a seleção.
4. Limpeza da seleção anterior ao mudar os filtros da sidebar.
5. Limites de 27 artistas nos dois dashboards e rolagem do ranking.

Resultado: conferência visual aprovada pela autoria. Esse registro corresponde
ao teste manual informado pela estudante, separado dos doze testes automatizados
aprovados na última execução registrada em 02/11/2026.
