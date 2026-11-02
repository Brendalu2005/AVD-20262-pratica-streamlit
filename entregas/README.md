# entregas/

Reuni nesta pasta os artefatos das entregas: rascunhos, justificativa das métricas,
validação e evidência da publicação. Mantenho os registros de uso de IA em
[`prompts/`](../prompts). Organizo os arquivos por aula, conforme o roteiro.

| Arquivo                      | Quando    | O que é                                                                                      |
|-------------------------------|-----------|-----------------------------------------------------------------------------------------------|
| `rascunho-dashboard1.jpg`/`.png`     | Aula 21   | Foto do rascunho do layout do Dashboard 1, feito antes de codar                               |
| `rascunho-dashboard2.jpg`/`.png`     | Aula 22   | Mesma ideia, para o Dashboard 2 — desenhado só depois de definir widgets, variáveis e métricas |
| `justificativa-metricas.md`   | Aula 22   | Por que cada métrica/KPI do Dashboard 2 foi escolhida e o que ela comunica ao público-alvo     |

## Checklist — Aula 21

- [x] `rascunho-dashboard1.png` — revisão para correlação e distribuição

## Checklist — Aula 22

- [x] `rascunho-dashboard2.png`
- [x] `justificativa-metricas.md` preenchido (não só criado vazio)

## Checklist — entrega final (Aula 23)

- [x] Os dois rascunhos
- [x] `justificativa-metricas.md` completo

## Histórico da revisão — 02/11/2026

Apresento os dois `rascunho-dashboard*.png` como revisões de 02/11/2026,
correspondentes às abas atuais e ao tema escuro/verde. Não os apresento como
evidência de planejamento anterior à implementação. Mantenho a imagem
inicialmente chamada `rascunho-dashboard1.png` em `proposta-inicial-spotify.png`:
ela representa a proposta inicial de KPIs e ranking. O wireframe do Dashboard 2
já existia antes desta revisão.

O Dashboard 1 reúne correlação, distribuição e controles de exploração;
o Dashboard 2 reúne quatro KPIs, seleção por gênero, ranking e dispersão.
O limite opcional de artistas fica na sidebar e afeta os dois dashboards.
O ranking mostra todos os artistas com streams válidos desse recorte, com rolagem.

- [x] Aprovei a revisão do aplicativo
- [x] Fiz commit e push da versão do aplicativo
- [x] Realizei a conferência visual e os cliques nos gráficos no navegador em 02/11/2026
- [ ] Declaração formal de IA preenchida e assinada
- [x] Publiquei o app e incluí o link no README principal
- [x] Incluí a evidência da publicação em `evidencia_app_publicado.jpg`
- [x] Testei a URL pública em janela anônima e confirmei o funcionamento de todos os itens em 02/11/2026

**Aplicação:** [Abrir o dashboard Spotify](https://brendalu2005-spotifystreamingperformance.streamlit.app/).
O registro da publicação e o escopo das verificações estão em [validacao.md](validacao.md).

## Modelo de `justificativa-metricas.md`

Cada métrica indica **a variável** a que se refere, **o que mede**, **por que foi escolhida** e **o que comunica** a um público que não precisa captar as nuances da variável.

```markdown
# Justificativa das métricas — Dashboard 2

## Métrica 1: <nome>
- **Variável:**
- **O que mede:**
- **Por que foi escolhida:**
- **O que comunica ao público-alvo:**
```

### Exemplo preenchido

```markdown
## Métrica: Distribuição do colesterol em relação à mediana
- **Variável:** `chol` (colesterol sérico, mg/dl)
- **O que mede:** a proporção de pessoas da amostra abaixo, em torno e acima da mediana de `chol`,
  junto de algumas estatísticas descritivas (média, mediana, mínimo, máximo, desvio padrão).
  "Em torno" = dentro de ±10% da mediana (defina e explicite a faixa que você usar).
- **Por que foi escolhida:** dá uma visão simplificada e direta da variável, sem exigir leitura
  de histograma ou boxplot.
- **O que comunica ao público-alvo:** como está distribuída a amostra de forma resumida
  (ex.: "metade das pessoas está acima de X mg/dl"), para quem não consegue captar as
  nuances da variável.
```
