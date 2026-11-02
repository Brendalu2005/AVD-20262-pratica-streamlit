"""Gera revisões dos wireframes, preservando a proposta inicial da autoria."""
from pathlib import Path
import shutil
import tomllib
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "entregas"
theme = tomllib.loads((ROOT / ".streamlit/config.toml").read_text(encoding="utf-8"))["theme"]
BG, PANEL, TEXT, ACCENT = [theme[key] for key in (
    "backgroundColor", "secondaryBackgroundColor", "textColor", "primaryColor")]


def font(size):
    for name in ("C:/Windows/Fonts/arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default(size=size)


def render(number):
    image = Image.new("RGB", (1560, 1080), BG)
    draw = ImageDraw.Draw(image)

    def box(rect, title, lines=()):
        draw.rounded_rectangle(rect, radius=12, fill=PANEL, outline=ACCENT, width=2)
        x, y, _, _ = rect
        draw.text((x + 18, y + 15), title, font=font(22), fill=ACCENT)
        for i, line in enumerate(lines):
            draw.text((x + 18, y + 55 + i * 30), line, font=font(19), fill=TEXT)

    draw.text((30, 18), f"Spotify | Dashboard {number} — revisão do layout", font=font(32), fill=ACCENT)
    draw.text((30, 65), "Revisão em 02/11/2026 para aprovação; documenta a implementação atual.", font=font(20), fill=TEXT)
    box((25, 115, 310, 1010), "Filtros compartilhados", [
        "Gêneros [multisseleção]", "Tipos [multisseleção]", "Ano de estreia [intervalo]", "",
        "Categorias vazias:", "nenhum artista", "", "Ano = estreia do artista;", "não é data dos streams.",
    ])
    active1, active2 = ("[ativo]", "") if number == 1 else ("", "[ativo]")
    box((335, 115, 1530, 180), f"Dashboard 1 · Exploração {active1}   |   Dashboard 2 · Indicadores {active2}")
    if number == 1:
        box((335, 205, 1530, 440), "Controles da exploração", [
            "Variáveis quantitativas [multisseleção]   |   Distinguir por gênero [liga/desliga]",
            "Método de correlação [Pearson / Spearman]",
            "Intervalos das variáveis selecionadas [expansor com sliders de intervalo]",
            "Filtros numéricos afetam somente o Dashboard 1.",
        ])
        box((335, 470, 850, 870), "Correlação", [
            "Heatmap + coeficientes + tooltip", "Calculada no recorte filtrado", "Escala fixa de -1 a 1", "",
            "0 variáveis: orientação de seleção", "1 variável: só distribuição", "Constantes: correlação indefinida",
        ])
        box((875, 470, 1530, 870), "Distribuição", [
            "Variável da distribuição [seletor]", "Número máximo de classes [5 a 60]", "Histograma de artistas",
            "Cor por gênero quando ativada", "Volumes de streams em milhões",
        ])
        draw.text((340, 910), "Sem artistas no recorte: aviso para ampliar os filtros. Correlação não implica causalidade.", font=font(20), fill=TEXT)
    else:
        box((335, 200, 1530, 275), "Artistas no ranking [slider de 5 a 20, nesta aba]")
        for i, title in enumerate(["Artistas", "Streams atribuídos", "Mediana / artista", "Top 5 (%)"]):
            x = 335 + i * 301
            box((x, 300, x + 287, 410), title, ["Valor do recorte"])
        box((335, 435, 1530, 660), "Streams por gênero — gráfico de seleção", [
            "Barras horizontais: soma de streams atribuídos em milhões por gênero",
            "Clique seleciona; Shift combina gêneros; duplo clique limpa a seleção.",
            "A seleção atualiza os quatro KPIs, o ranking e a dispersão.",
            "Sem seleção = todos os artistas dos filtros compartilhados.",
        ])
        box((335, 690, 910, 915), "Top N artistas por streams", ["Barras em milhões", "Ordem do maior para o menor", "Top N não altera os KPIs."])
        box((935, 690, 1530, 915), "Principal × participação", ["Dispersão por artista e gênero", "Tooltip: artista e volumes em milhões", "Zoom e deslocamento interativos"])
        draw.text((340, 950), "Volumes acumulados atribuídos; a soma não mede streams únicos da plataforma.", font=font(20), fill=TEXT)
        draw.text((340, 985), "Recorte vazio: contagem 0, demais KPIs 'Sem dados' e aviso nos gráficos.", font=font(20), fill=TEXT)
    image.save(DEST / f"rascunho-dashboard{number}.png")


if __name__ == "__main__":
    initial = DEST / "proposta-inicial-spotify.png"
    if not initial.exists():
        shutil.copy2(DEST / "rascunho-dashboard1.png", initial)
    for number in (1, 2):
        render(number)
