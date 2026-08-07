#!/usr/bin/env python3
"""
Final two artworks, emitted as theme-aware inline SVG.

  hero   — loss landscape with a gradient-descent path (option 6)
  accent — vector field with streamlines (option 5), smaller, for mid-page

Colours are CSS custom properties so both retheme with the page in dark mode.
"""
import math
import random
import tempfile

DEST = str(__import__("pathlib").Path(__file__).parent.parent / "assets") + "/"

INK, TERRA, BLUE, TEAL, MUSTARD, SILVER = (
    "var(--art-ink)", "var(--art-terra)", "var(--art-blue)",
    "var(--art-teal)", "var(--art-mustard)", "var(--art-silver)")
RED = "@media(prefers-reduced-motion:reduce){*{animation:none!important}}"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

# Self-contained palette: these files are loaded via <img>, so they cannot
# inherit the page's custom properties and must define their own.
PALETTE = """
    :root{--art-ink:#253342;--art-terra:#c05c3e;--art-blue:#7fa8cd;
          --art-teal:#4a8b8b;--art-mustard:#d9a441;--art-silver:#aab4be}
    @media(prefers-color-scheme:dark){
      :root{--art-ink:#c6d2dd;--art-terra:#d9836b;--art-blue:#6d93b8;
            --art-teal:#5d9c9c;--art-mustard:#c9a05a;--art-silver:#7e878f}
    }"""


# ═════════════════════════════════════════════════ hero: loss landscape ═══
def hero():
    W, H = 580, 400
    MX, MY = 290, 200          # the minimum
    ROT = -24
    A, B = 250.0, 118.0        # bowl semi-axes; A/B sets the condition number
    o = [f'<svg class="hero-art" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
         f'role="img" aria-label="A loss landscape drawn as nested contours, with a '
         f'gradient-descent path zig-zagging down into the minimum">']
    # NOTE: every resting state below is the *finished* drawing. Animation is
    # purely additive, so the artwork still reads correctly wherever CSS
    # animation does not run — reduced-motion, some <img> contexts, printing.
    o.append(f'''<style>{PALETTE}
    .pth{{stroke-dasharray:var(--l);stroke-dashoffset:0;opacity:.9;
         animation:go 7s ease-in-out infinite}}
    @keyframes go{{0%{{stroke-dashoffset:var(--l)}}
      55%,100%{{stroke-dashoffset:0}}}}
    .stp{{opacity:.9;animation:stp 7s ease-in-out infinite}}
    @keyframes stp{{0%,2%{{opacity:0}}9%,100%{{opacity:.9}}}}
    .mk{{opacity:1;transform-box:fill-box;transform-origin:center;
        animation:mk 7s ease-in-out infinite}}
    @keyframes mk{{0%,52%{{opacity:0;transform:scale(.4)}}
      62%,100%{{opacity:1;transform:scale(1)}}}}
    .halo{{opacity:0;transform-box:fill-box;transform-origin:center;
          animation:hal 7s ease-in-out infinite}}
    @keyframes hal{{0%,54%{{opacity:0;transform:scale(.5)}}
      68%{{opacity:.6;transform:scale(1)}}84%,100%{{opacity:0;transform:scale(2)}}}}
    .cn{{animation:cn 8s ease-in-out infinite}}
    @keyframes cn{{0%,100%{{opacity:.28}}50%{{opacity:.72}}}}
    .gr{{animation:gr 8s ease-in-out infinite}}
    @keyframes gr{{0%,100%{{opacity:.14}}50%{{opacity:.55}}}}
    {RED}</style>''')

    cs, sn = math.cos(math.radians(ROT)), math.sin(math.radians(ROT))

    def to_screen(u, v):
        """Bowl-local coords -> screen."""
        return MX + u * cs - v * sn, MY + u * sn + v * cs

    # ── contours ──────────────────────────────────────────────────────────
    N = 13
    for i in range(N, 0, -1):
        t = i / N
        rx, ry = 22 + t * (A - 22), 14 + t * (B - 14)
        if i > 8:    col, op, dl = BLUE,  0.22, i * 0.18
        elif i > 5:  col, op, dl = TEAL,  0.32, i * 0.18
        elif i > 2:  col, op, dl = TERRA, 0.40, i * 0.18
        else:        col, op, dl = TERRA, 0.58, i * 0.18
        o.append(f'<ellipse cx="{MX}" cy="{MY}" rx="{rx:.0f}" ry="{ry:.0f}" fill="none" '
                 f'stroke="{col}" stroke-width="{1.5 if i <= 2 else 1}" opacity="{op}" '
                 f'transform="rotate({ROT} {MX} {MY})"/>')
    o.append(f'<ellipse cx="{MX}" cy="{MY}" rx="26" ry="16" fill="{TERRA}" opacity="0.15" '
             f'transform="rotate({ROT} {MX} {MY})"/>')

    # ── downhill gradient arrows ──────────────────────────────────────────
    rnd = random.Random(12)
    for _ in range(18):
        ang, rad = rnd.uniform(0, math.tau), rnd.uniform(0.45, 1.02)
        u, v = A * rad * math.cos(ang), B * rad * math.sin(ang)
        x, y = to_screen(u, v)
        if not (18 < x < W - 18 and 22 < y < H - 26):
            continue
        # -∇f in bowl coords, mapped back to the screen
        gu, gv = -u / (A * A), -v / (B * B)
        gx, gy = gu * cs - gv * sn, gu * sn + gv * cs
        n = math.hypot(gx, gy) or 1
        dx, dy, L = gx / n, gy / n, 13
        tx, ty = x + dx * L, y + dy * L
        h = []
        for a in (2.55, -2.55):                      # arrowhead barbs
            ca, sa = math.cos(a), math.sin(a)
            h.append(f'M{tx:.1f},{ty:.1f} l{(dx*ca-dy*sa)*5.2:.1f},{(dx*sa+dy*ca)*5.2:.1f}')
        o.append(f'<path d="M{x:.1f},{y:.1f} L{tx:.1f},{ty:.1f} {" ".join(h)}" fill="none" '
                 f'stroke="{INK}" stroke-width="0.95" stroke-linecap="round" class="gr"/>')

    # ── gradient descent, actually simulated ──────────────────────────────
    lr = 1.60 * B * B
    u, v = -0.86 * A, 0.40 * B      # start inside the outermost contour
    assert (u / A) ** 2 + (v / B) ** 2 < 1, "start point sits outside the bowl"
    pts = [to_screen(u, v)]
    for _ in range(11):
        u -= lr * u / (A * A)
        v -= lr * v / (B * B)
        pts.append(to_screen(u, v))
    bx = [p[0] for p in pts]; by = [p[1] for p in pts]
    print(f"  descent bbox x[{min(bx):.0f},{max(bx):.0f}] y[{min(by):.0f},{max(by):.0f}] "
          f"in {W}x{H}")

    d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    L = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2.1" '
             f'stroke-linejoin="round" stroke-linecap="round" opacity="0.9" '
             f'class="pth" style="--l:{L:.0f}"/>')
    for i, (a, b) in enumerate(pts[:-2]):
        o.append(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="{4.8 if i == 0 else 3.2}" '
                 f'fill="{INK}" class="stp" style="animation-delay:{i*0.24:.2f}s"/>')

    # ── the minimum ───────────────────────────────────────────────────────
    o.append(f'<circle cx="{MX}" cy="{MY}" r="15" fill="none" stroke="{TERRA}" '
             f'stroke-width="1.4" class="halo"/>')
    o.append(f'<circle cx="{MX}" cy="{MY}" r="6.4" fill="{TERRA}" class="mk"/>')

    # travelling pulses riding two of the contours
    for j, (ri, dur, dly) in enumerate(((6, 9.0, 0.0), (10, 13.0, 3.2))):
        t = ri / N
        prx, pry = 22 + t * (A - 22), 14 + t * (B - 14)
        o.append(f'<ellipse id="cn{j}" cx="{MX}" cy="{MY}" rx="{prx:.0f}" ry="{pry:.0f}" '
                 f'fill="none" stroke="none" transform="rotate({ROT} {MX} {MY})"/>')
        o.append(f'<circle r="3" fill="{TERRA}" opacity="0.85">'
                 f'<animateMotion dur="{dur}s" begin="{dly}s" repeatCount="indefinite" '
                 f'rotate="auto"><mpath href="#cn{j}"/></animateMotion></circle>')

    o.append(f'<text x="{W-22}" y="{H-20}" text-anchor="end" font-size="11" '
             f'letter-spacing="2.4" fill="{SILVER}" font-family="{MONO}" '
             f'opacity="0.7">argmin</text>')
    return "\n".join(o) + "\n</svg>\n"


# ══════════════════════════════════════════════ accent: vector field ══════
def accent():
    W, H = 400, 320
    o = [f'<svg class="accent-art" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
         f'role="img" aria-label="A vector field with particle streamlines flowing through it">']
    o.append(f'''<style>{PALETTE}
    .tick{{animation:tk 7s ease-in-out var(--d) infinite}}
    @keyframes tk{{0%,100%{{opacity:.14}}50%{{opacity:.46}}}}
    .puls{{opacity:.9;animation:pu 4.2s linear var(--d) infinite}}
    @keyframes pu{{0%{{opacity:0}}8%{{opacity:.95}}70%{{opacity:.95}}100%{{opacity:0}}}}
    {RED}</style>''')

    def vec(x, y):
        u = math.sin(y / 58) + 0.62 * math.cos((x + y) / 76)
        v = math.cos(x / 64) - 0.5 * math.sin((x - y) / 82)
        n = math.hypot(u, v) or 1
        return u / n, v / n

    rnd = random.Random(8)
    for gx in range(22, W - 12, 26):
        for gy in range(20, H - 12, 26):
            u, v = vec(gx, gy)
            o.append(f'<line x1="{gx}" y1="{gy}" x2="{gx+u*9:.1f}" y2="{gy+v*9:.1f}" '
                     f'stroke="{INK}" stroke-width="0.7" opacity="0.18" class="tick" '
                     f'style="--d:{rnd.uniform(0,6):.1f}s"/>')

    cols = [INK, TERRA, BLUE, TEAL, MUSTARD]
    for k in range(20):
        x, y = rnd.uniform(16, W - 16), rnd.uniform(16, H - 16)
        pts = [(x, y)]
        for _ in range(70):
            u, v = vec(x, y); x += u * 3.6; y += v * 3.6
            if not (4 < x < W - 4 and 4 < y < H - 4):
                break
            pts.append((x, y))
        if len(pts) < 14:
            continue
        d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)
        c = cols[k % len(cols)]
        # streamlines stay drawn; a pulse travels along them
        o.append(f'<path id="s{k}" d="{d}" fill="none" stroke="{c}" stroke-width="1.4" '
                 f'stroke-linecap="round" opacity="0.6"/>')
        o.append(f'<circle r="2.4" fill="{c}" class="puls" style="--d:{k*0.22:.2f}s">'
                 f'<animateMotion dur="4.2s" begin="{k*0.22:.2f}s" repeatCount="indefinite">'
                 f'<mpath href="#s{k}"/></animateMotion></circle>')
    return "\n".join(o) + "\n</svg>\n"


# ══════════════════════════════════════════════ lorenz attractor ═════════
def lorenz():
    """Same aspect ratio as accent(), so the two stack cleanly."""
    W, H = 400, 320
    s, r, b, dt = 10.0, 28.0, 8 / 3, 0.0045
    x, y, z = 0.1, 0.0, 0.0
    pts = []
    for i in range(14000):
        x += s * (y - x) * dt
        y += (x * (r - z) - y) * dt
        z += (x * y - b * z) * dt
        if i > 400:
            pts.append((x, z))
    xs, zs = [p[0] for p in pts], [p[1] for p in pts]
    x0, x1, z0, z1 = min(xs), max(xs), min(zs), max(zs)
    sc = min((W - 46) / (x1 - x0), (H - 52) / (z1 - z0))

    def T(p):
        return ((p[0] - x0) * sc + (W - (x1 - x0) * sc) / 2,
                H - 26 - (p[1] - z0) * sc)

    o = [f'<svg class="accent-art" viewBox="0 0 {W} {H}" '
         f'xmlns="http://www.w3.org/2000/svg" role="img" '
         f'aria-label="The Lorenz attractor, traced as a single continuous curve">']
    o.append(f'''<style>{PALETTE}
    .lz{{stroke-dasharray:9000;stroke-dashoffset:0;
        animation:tr 14s ease-out infinite}}
    @keyframes tr{{0%{{stroke-dashoffset:9000}}62%,100%{{stroke-dashoffset:0}}}}
    .fp{{animation:fp 3.2s ease-in-out infinite}}
    @keyframes fp{{0%,100%{{opacity:.85;r:4.4}}50%{{opacity:.35;r:6.6}}}}
    {RED}</style>''')
    o.append(f'<defs><linearGradient id="lzg" x1="0" y1="0" x2="1" y2="1">'
             f'<stop offset="0%" stop-color="{BLUE}"/>'
             f'<stop offset="52%" stop-color="{INK}"/>'
             f'<stop offset="100%" stop-color="{TERRA}"/></linearGradient></defs>')
    d = "M" + " L".join(f"{T(p)[0]:.1f},{T(p)[1]:.1f}" for p in pts[::3])
    o.append(f'<path d="{d}" fill="none" stroke="url(#lzg)" stroke-width="0.85" '
             f'opacity="0.82" stroke-linejoin="round" class="lz"/>')
    for fx in (-1, 1):                              # the two fixed points
        px, py = T((fx * math.sqrt(b * (r - 1)), r - 1))
        o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.4" fill="{TERRA}" '
                 f'class="fp" style="animation-delay:{0 if fx < 0 else 1.6}s"/>')
    o.append(f'<text x="{W-14}" y="{H-10}" text-anchor="end" font-size="10" '
             f'letter-spacing="2" fill="{SILVER}" font-family="{MONO}" '
             f'opacity="0.7">σ=10 ρ=28 β=8/3</text>')
    return "\n".join(o) + "\n</svg>\n"


open(DEST + "hero.svg", "w", encoding="utf-8").write(hero())
open(DEST + "accent.svg", "w", encoding="utf-8").write(accent())
open(DEST + "lorenz.svg", "w", encoding="utf-8").write(lorenz())

# The side-by-side preview is a debugging aid, not part of the site — keep it
# out of the repo so it never ends up committed or published.
_PREV = tempfile.gettempdir() + "/"

prev = """<!doctype html><meta charset="utf-8"><style>
:root{--art-ink:#253342;--art-terra:#c05c3e;--art-blue:#7fa8cd;--art-teal:#4a8b8b;
--art-mustard:#d9a441;--art-silver:#aab4be;--mono:ui-monospace,Menlo,monospace}
body{background:#fefdf9;margin:0;padding:20px;font:13px ui-sans-serif,system-ui;color:#253342}
.card{background:#fdfcf8;border:1px solid rgba(39,55,70,.14);border-radius:5px;
      padding:10px 14px 14px;margin-bottom:16px}
.lbl{font:10.5px ui-monospace,Menlo,monospace;letter-spacing:.14em;text-transform:uppercase;
     color:#87919c;margin-bottom:3px}
.hero-art{width:540px;height:auto;display:block}
.accent-art{width:400px;height:auto;display:block}
</style>
<div class="card"><div class="lbl">hero — loss landscape</div>""" + hero() + """</div>
<div class="card"><div class="lbl">accent — vector field</div>""" + accent() + "</div>"
open(_PREV + "art-preview.html", "w", encoding="utf-8").write(prev)
print(f"wrote {DEST}hero.svg, {DEST}accent.svg  (preview: {_PREV}art-preview.html)")
