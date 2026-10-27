"""Gera um wireframe de layout com Pillow; executar na raiz do projeto."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
image = Image.new("RGB", (1440, 980), "#FFF9F2")
draw = ImageDraw.Draw(image)
font_path = "C:/Windows/Fonts/arial.ttf"
def font(size):
    try:
        return ImageFont.truetype(font_path, size)
    except OSError:
        return ImageFont.load_default(size=size)

def box(rect, title, lines=()):
    draw.rounded_rectangle(rect, radius=12, fill="white", outline="#DBBFA5", width=2)
    x, y, _, _ = rect
    draw.text((x + 18, y + 15), title, font=font(21), fill="#9C3D10")
    for index, line in enumerate(lines):
        draw.text((x + 18, y + 55 + index * 31), line, font=font(18), fill="#34281F")

draw.text((30, 20), "Spotify | Rascunho do Dashboard 2", font=font(32), fill="#9C3D10")
draw.text((30, 65), "Planejamento: variáveis > métricas > widgets > layout > implementação", font=font(20), fill="#34281F")
box((25, 115, 305, 910), "Filtros compartilhados", ["Gêneros [multisseleção]", "Tipos [multisseleção]", "Ano de estreia [intervalo]", "", "Dashboard 2:", "Ranking [5 a 20]", "", "Categorias vazias:", "nenhum artista", "", "Ano = estreia do artista", "e não data dos streams"])
box((330, 115, 1410, 180), "Dashboard 1: exploração  |  Dashboard 2: indicadores [ativo]")
titles = ["Artistas", "Streams atribuídos", "Mediana / artista", "Top 5 (%)"]
for i, title in enumerate(titles):
    x = 330 + i * 273
    box((x, 200, x + 260, 310), title, ["Valor do recorte"])
box((330, 335, 1410, 565), "Streams por gênero — gráfico de seleção", ["Barras horizontais | clique seleciona; Shift adiciona; duplo clique limpa", "Seleção atualiza os quatro KPIs, ranking e dispersão", "Sem seleção = todos os artistas dos filtros laterais"])
for i, width in enumerate([580, 440, 320]):
    draw.rectangle((355, 475 + i * 24, 355 + width, 490 + i * 24), fill="#C65318")
box((330, 590, 850, 845), "Top N artistas", ["Barras de streams em milhões", "Ordenadas do maior para o menor"])
box((875, 590, 1410, 845), "Principal × participação", ["Dispersão por artista e gênero", "Tooltip: nome e volumes (milhões)"])
draw.text((335, 870), "Nota: volumes acumulados atribuídos; soma não equivale a streams únicos.", font=font(19), fill="#34281F")
draw.text((335, 905), "Recorte vazio: contagem 0, demais KPIs 'Sem dados' e aviso nos gráficos.", font=font(19), fill="#34281F")
image.save(ROOT / "entregas/rascunho-dashboard2.png")
