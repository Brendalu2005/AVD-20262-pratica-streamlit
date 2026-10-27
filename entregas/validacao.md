# Validação dos dashboards

Comando: `python -m unittest discover -s tests -v`.
Resultado em 27/10/2026: seis testes aprovados com unittest e Streamlit AppTest.

- Dashboard 1: seleção de zero, uma, duas e quatro variáveis; avisos adequados sem exceções.
- Distribuição: alternância de variável, quantidade de classes e distinção por gênero.
- Correlação: Pearson e Spearman; valor calculado no recorte confrontado com pandas, diferente da base completa; variáveis constantes resultam em tabela vazia, sem correlação inventada.
- Filtros: gêneros/tipos vazios, ano de estreia e intervalo numérico que deixa um único registro.
- KPIs: soma, mediana e proporção Top 5 comparadas com valores conhecidos; denominador zero e recorte vazio tratados.
- Seleção: função que aplica o payload do clique validada para nenhum, um e múltiplos gêneros.
- Ranking: alterar Top N não altera os KPIs do recorte.
- Entradas: `app.py` e `app_spotify.py` renderizam duas abas sem exceções.

O AppTest valida execução e widgets, mas não simula o gesto de clique no canvas do Vega no navegador. O encadeamento usa o padrão do guia local: seleção nomeada por campo, `on_select="rerun"`, payload aplicado no Python e gráficos secundários construídos com os dados selecionados. O rascunho PNG foi inspecionado visualmente.
