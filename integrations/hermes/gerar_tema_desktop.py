# Gera desktop-theme.dbmo.json: paleta prata + customCSS (desktop-theme.dbmo.css) com o sprite
# dos rostos de d-BMO-body/firmware/rosto/rosto_faces.h.
# Uso: python3 integrations/hermes/gerar_tema_desktop.py ~/d-BMO-body/firmware/rosto/rosto_faces.h
import json, pathlib, re, struct, sys, urllib.parse, zlib
faces_h = sys.argv[1]
here = pathlib.Path(__file__).parent
css_in, out = here / "desktop-theme.dbmo.css", here / "desktop-theme.dbmo.json"
avatar_out = here / "avatar-dbmo.png"
src = open(faces_h).read()
faces = {}
for name, body in re.findall(r"const Frame ROSTO_(\w+)\[\] = \{(.*?)\n\};", src, re.S):
    frames = []
    for rows, ms in re.findall(r"\{\{(.*?)\},\s*(\d+)\}", body, re.S):
        grid = ["." * 16 if r == "VAZIO" else r.strip('"') for r in re.findall(r'"[.#+]{16}"|VAZIO', rows)]
        assert len(grid) == 12, (name, len(grid))
        frames.append((grid, int(ms)))
    faces[name] = frames

# Roteiro em segundos: (rosto, tempo em tela). Sem ALERT/ERROR/OFFLINE: num loop ocioso assustariam.
ROTEIRO = [("IDLE", 6.5), ("THINKING", 2.4), ("IDLE", 2.5), ("CURIOUS", 3.0), ("SCANNING", 2.4),
           ("ANALYZING", 2.4), ("SUCCESS", 3.0), ("IDLE", 5.5), ("PROTECTING", 2.8), ("IDLE", 3.0)]

sprite, index = [], {}
def frame_id(grid):
    key = "".join(grid)
    if key not in index:
        index[key] = len(sprite); sprite.append(grid)
    return index[key]

timeline = []  # (frame, segundos)
for face, hold in ROTEIRO:
    t, i = 0.0, 0
    while t < hold - 1e-9:
        grid, ms = faces[face][i % len(faces[face])]
        d = min(ms / 1000, hold - t)
        timeline.append((frame_id(grid), d)); t += d; i += 1

def paths(color_char):
    d = []
    for k, grid in enumerate(sprite):
        for y, row in enumerate(grid):
            for m in re.finditer(re.escape(color_char) + "+", row):
                d.append(f"M{k*16+m.start()} {y}h{m.end()-m.start()}v1h-{m.end()-m.start()}z")
    return "".join(d)
n = len(sprite)
red, dark = paths("#"), paths("+")
svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {16*n} 12' shape-rendering='crispEdges'>"
       f"<filter id='g' x='-5%' y='-20%' width='110%' height='140%'><feGaussianBlur stdDeviation='0.45'/></filter>"
       f"<path filter='url(#g)' opacity='0.7' fill='#FF2E3F' d='{red}'/>"
       f"<path fill='#8F1722' d='{dark}'/><path fill='#D92332' d='{red}'/></svg>")
uri = "data:image/svg+xml," + urllib.parse.quote(svg, safe="/:=' ")

total = sum(d for _, d in timeline)
kf, t = [], 0.0
for frame, d in timeline:
    x = 0 if n == 1 else frame / (n - 1) * 100
    kf.append(f"  {t/total*100:.3f}% {{ background-position: 0 0, {x:.4f}% 0, 0 0; animation-timing-function: steps(1, end); }}")
    t += d
kf.append(f"  100% {{ background-position: 0 0, 0% 0, 0 0; }}")
css = (open(css_in).read().replace("SPRITE_W", f"{n*100}%").replace("SPRITE", uri)
       .replace("DURATION", f"{total:.1f}").replace("KEYFRAMES", "@keyframes dbmo-face {\n" + "\n".join(kf) + "\n}"))

palette = {
    "background": "#D5D7D9", "foreground": "#16181B", "card": "#E3E5E7", "cardForeground": "#16181B",
    "muted": "#C9CDD1", "mutedForeground": "#4A4F55", "popover": "#ECEEF0", "popoverForeground": "#16181B",
    "primary": "#D92332", "primaryForeground": "#FFFFFF", "secondary": "#E2C9CC", "secondaryForeground": "#16181B",
    "accent": "#E4D2D4", "accentForeground": "#16181B", "border": "#AEB3B8", "input": "#E9EBED",
    "ring": "#D92332", "midground": "#D92332", "midgroundForeground": "#FFFFFF", "composerRing": "#D92332",
    "destructive": "#B3261E", "destructiveForeground": "#FFFFFF", "sidebarBackground": "#CDD0D3",
    "sidebarBorder": "#AEB3B8", "userBubble": "#E9EBED", "userBubbleBorder": "#C2C6CA"}
theme = {"name": "dbmo", "label": "d-BMO", "description": "BE MORE DARK: prata espelhada, vidro e vermelho sinal",
         "colors": palette, "darkColors": palette, "customCSS": css}
json.dump(theme, open(out, "w"), ensure_ascii=False, indent=2); open(out, "a").write("\n")
print(f"{n} quadros, {len(timeline)} trocas, ciclo {total:.1f}s, customCSS {len(css.encode())} bytes")

# Avatar do bot (256 × 256): rosto IDLE recortado com 2 blocos de margem, sobre tela escura.
# Enviar pelo app: Bots > botão direito no bot > Edit… > Upload.
def png(path, w, h, pixel):
    raw = b"".join(b"\0" + b"".join(bytes(pixel(x, y)) for x in range(w)) for y in range(h))
    chunk = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d))
    path.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
                     + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))

idle = faces["IDLE"][0][0]
cells = [(x, y) for y, row in enumerate(idle) for x, c in enumerate(row) if c != "."]
x0, y0 = min(x for x, _ in cells) - 2, min(y for _, y in cells) - 2
side = max(max(x for x, _ in cells) - x0 + 3, max(y for _, y in cells) - y0 + 3)
EDGE = 256
cell = EDGE / side
ox, oy = x0 - (side - (max(x for x, _ in cells) - x0 + 3)) / 2, y0 - (side - (max(y for _, y in cells) - y0 + 3)) / 2
COR = {"#": (217, 35, 50), "+": (143, 23, 34)}
def pixel(x, y):
    gx, gy = int(ox + x / cell), int(oy + y / cell)
    c = idle[gy][gx] if 0 <= gy < 12 and 0 <= gx < 16 else "."
    if c in COR:
        return (*COR[c], 255)
    d = ((x - EDGE / 2) ** 2 + (y - EDGE * 0.42) ** 2) ** 0.5 / EDGE  # tela: centro grafite, borda preta
    k = max(0.0, 1 - d * 1.6)
    return (int(7 + 16 * k), int(8 + 17 * k), int(9 + 19 * k), 255)
png(avatar_out, EDGE, EDGE, pixel)
print(f"avatar {avatar_out.name}: {EDGE}x{EDGE}")
