import math, os, subprocess, wave, random
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
WHITE = (245, 245, 250); LIME = (198, 255, 61); VIO = (124, 92, 255)
BLUE = (80, 140, 255); TEAL = (61, 214, 200); RED = (255, 77, 94)
GREY = (150, 150, 178); DARK = (12, 12, 20); CARD = (26, 24, 48); ORANGE = (255, 170, 60)
FD = "/usr/share/fonts/opentype/inter/"
BLK, BLD, SEM, MED = "InterDisplay-Black.otf", "Inter-Bold.otf", "Inter-SemiBold.otf", "Inter-Medium.otf"

@lru_cache(None)
def FT(name, size):
    return ImageFont.truetype(FD + name if os.path.exists(FD + name) else FD + "Inter-Bold.otf", int(size))

@lru_cache(None)
def fit(name, s, size, maxw):
    while FT(name, size).getlength(s) > maxw and size > 20: size -= 2
    return size

def clamp(x): return max(0.0, min(1.0, x))
def eo(x): x = clamp(x); return 1 - (1 - x) ** 3
def eb(x):
    x = clamp(x); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2
def prog(t, s, d=0.5): return clamp((t - s) / d)
def spaced(s): return " ".join(s)
def fmt(n): return f"{int(round(n)):,}".replace(",", " ")

SA = 1.0
_tc = {}
def tmask(s, f):
    k = (s, id(f))
    if k not in _tc:
        bb = f.getbbox(s); a, d = f.getmetrics()
        m = Image.new("L", (bb[2] - bb[0] + 6, a + d + 4), 0)
        ImageDraw.Draw(m).text((-bb[0] + 3, 2), s, font=f, fill=255)
        _tc[k] = m
    return _tc[k]

def mult(m, a): return m if a >= 0.999 else m.point(lambda v: int(v * a))

def text(fr, s, fname, size, cx, cy, color, a=1.0, anchor="c", maxw=None):
    a *= SA
    if a <= 0.01 or not s: return
    size = int(size)
    if maxw: size = fit(fname, s, size, maxw)
    m = tmask(s, FT(fname, size))
    x = cx - m.width / 2 if anchor == "c" else (cx if anchor == "l" else cx - m.width)
    fr.paste(color, (int(x), int(cy - m.height / 2)), mult(m, a))

def shape(fr, box, color, a, fn):
    a *= SA
    if a <= 0.01: return
    x0, y0, x1, y1 = [int(round(v)) for v in box]
    w, h = max(1, x1 - x0), max(1, y1 - y0)
    m = Image.new("L", (w, h), 0); fn(ImageDraw.Draw(m), w, h)
    fr.paste(color, (x0, y0), mult(m, a))

def rrect(fr, box, color, a=1.0, r=30, outline=0):
    r = int(min(r, (box[3] - box[1]) / 2, (box[2] - box[0]) / 2))
    if outline: shape(fr, box, color, a, lambda d, w, h: d.rounded_rectangle((0, 0, w - 1, h - 1), radius=r, outline=255, width=outline))
    else: shape(fr, box, color, a, lambda d, w, h: d.rounded_rectangle((0, 0, w - 1, h - 1), radius=r, fill=255))

def circle(fr, cx, cy, r, color, a=1.0, outline=0):
    box = (cx - r, cy - r, cx + r + 1, cy + r + 1)
    if outline: shape(fr, box, color, a, lambda d, w, h: d.ellipse((0, 0, w - 1, h - 1), outline=255, width=outline))
    else: shape(fr, box, color, a, lambda d, w, h: d.ellipse((0, 0, w - 1, h - 1), fill=255))

def partial(pts, frac):
    if frac <= 0: return pts[:1]
    segs = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    tot = sum(segs) * frac; out = [pts[0]]
    for i, s in enumerate(segs):
        if tot >= s: out.append(pts[i + 1]); tot -= s
        else:
            r = tot / s
            out.append((pts[i][0] + (pts[i + 1][0] - pts[i][0]) * r, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * r)); break
    return out

def polyline(fr, pts, color, a, width):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]; pad = width + 4
    x0, y0 = min(xs) - pad, min(ys) - pad
    loc = [(x - x0, y - y0) for x, y in pts]
    def fn(d, w, h):
        if len(loc) > 1: d.line(loc, fill=255, width=width, joint="curve")
        for p in (loc[0], loc[-1]): d.ellipse((p[0] - width / 2, p[1] - width / 2, p[0] + width / 2, p[1] + width / 2), fill=255)
    shape(fr, (x0, y0, max(xs) + pad, max(ys) + pad), color, a, fn)

def polygon(fr, pts, color, a):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]; x0, y0 = min(xs), min(ys)
    loc = [(x - x0, y - y0) for x, y in pts]
    shape(fr, (x0, y0, max(xs) + 1, max(ys) + 1), color, a, lambda d, w, h: d.polygon(loc, fill=255))

def heading(fr, t, s, sub=None, y=400):
    p = eo(prog(t, 0.05)); text(fr, s, BLK, 96, 540, y + (1 - p) * 50, WHITE, p, maxw=980)
    if sub:
        p = eo(prog(t, 0.25)); text(fr, sub, MED, 44, 540, y + 100 + (1 - p) * 40, GREY, p, maxw=980)

def foot(fr, t, s, st):
    if s: text(fr, s, MED, 30, 540, 1720, GREY, eo(prog(t, st)) * 0.8)

# ---------------- background ----------------
yy = np.linspace(0, 1, H)[:, None, None]
BASE = np.repeat((np.array([16, 13, 34]) * (1 - yy) + np.array([5, 5, 11]) * yy), W, axis=1).astype(np.int16)
def _glow(size, color, s):
    r = np.linspace(-1, 1, size); d = np.sqrt(r[None, :] ** 2 + r[:, None] ** 2)
    return (np.exp(-(d / 0.5) ** 2)[..., None] * s * np.array(color)[None, None, :]).astype(np.int16)
G1 = _glow(1300, VIO, 0.55); G2 = _glow(1100, LIME, 0.22)
def _add_glow(arr, g, cx, cy):
    s = g.shape[0]; x0, y0 = int(cx - s / 2), int(cy - s / 2)
    ax0, ay0, ax1, ay1 = max(0, x0), max(0, y0), min(W, x0 + s), min(H, y0 + s)
    if ax1 > ax0 and ay1 > ay0: arr[ay0:ay1, ax0:ax1] += g[ay0 - y0:ay1 - y0, ax0 - x0:ax1 - x0]
def background(t):
    arr = BASE.copy()
    _add_glow(arr, G1, 540 + 380 * math.sin(t * 0.35), 500 + 250 * math.cos(t * 0.27))
    _add_glow(arr, G2, 540 - 360 * math.sin(t * 0.3 + 1), 1500 + 200 * math.sin(t * 0.4))
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")
    d = ImageDraw.Draw(img); sp = 120; off = (t * 24) % sp
    for x in range(0, W + sp, sp): d.line((x, 0, x, H), fill=(28, 26, 48), width=1)
    y = -sp + off
    while y < H: d.line((0, y, W, y), fill=(28, 26, 48), width=1); y += sp
    return img

# ---------------- templates: each returns (dur, draw_fn, events) ----------------
random.seed(4)
DOWN = [(110 + i * 78, 1400 + i * 22 + random.uniform(-40, 40) + (i * i) * 1.2) for i in range(12)]; DOWN[0] = (110, 1390)
UP = [(130 + i * 75, 970 - (i ** 1.7) * 6 + (20 if i % 3 == 1 else 0)) for i in range(12)]

def T_hook(tag, lines, chart=None, dur=3.5):
    hs = [l[2] * 1.18 for l in lines]; total = sum(hs)
    top = 640 if chart else 940 - total / 2
    ys = []; y = top
    for h in hs: ys.append(y + h / 2); y += h
    def fn(fr, t):
        full = spaced(tag); sz = fit(SEM, full, 34, 980)
        k = int(round(len(full) * clamp(t / 0.6)))
        if k > 0:
            x0 = 540 - FT(SEM, sz).getlength(full) / 2
            text(fr, full[:k], SEM, sz, x0, top - 70, LIME, 1, anchor="l")
        for i, (s, col, sz, pop) in enumerate(lines):
            st = 0.15 + 0.35 * i
            if pop:
                p = prog(t, st, 0.45)
                if p > 0: text(fr, s, BLK, max(30, sz * (0.55 + 0.45 * eb(p))), 540, ys[i], col, clamp(p * 2), maxw=980)
            else:
                p = eo(prog(t, st)); text(fr, s, BLK if sz >= 100 else BLD, sz, 540, ys[i] + (1 - p) * 60, col, p, maxw=980)
        if chart:
            lab, val = chart
            pa = eo(prog(t, 0.5, 0.4)); text(fr, lab, SEM, 40, 110, 1320, GREY, pa, anchor="l")
            pts = partial(DOWN, eo(prog(t, 0.7, 1.8)))
            if len(pts) > 1:
                polyline(fr, pts, RED, 0.95, 12); ex, ey = pts[-1]
                circle(fr, ex, ey, 30, RED, 0.25); circle(fr, ex, ey, 14, RED, 1)
            text(fr, val, BLK, 72, 970, 1320, RED, eo(prog(t, 2.2, 0.4)), anchor="r")
    ev = [(0.6 * i / max(1, len(tag)), "key", None) for i in range(len(tag)) if tag[i] != " "]
    for i, l in enumerate(lines):
        st = 0.15 + 0.35 * i
        ev += [(st, "pop", 700)] if l[3] else [(st, "swish", None), (st, "tick", None)]
    if chart: ev += [(0.7, "sweep", (1.8, 520, 140, 0.10)), (2.2, "thud", None)]
    return dur, fn, ev

def T_title(tag, big1, big2, sub, chips=None, dur=4.0):
    def fn(fr, t):
        p = eo(prog(t, 0.1)); text(fr, spaced(tag), SEM, 38, 540, 690 + (1 - p) * 40, LIME, p)
        p = eo(prog(t, 0.3, 0.55)); text(fr, big1, BLK, 150, 540 - (1 - p) * 300, 840, WHITE, p, maxw=980)
        p = eo(prog(t, 0.45, 0.55)); text(fr, big2, BLK, 150, 540 + (1 - p) * 300, 990, LIME, p, maxw=980)
        p = eo(prog(t, 0.8, 0.6))
        if p > 0: rrect(fr, (540 - 220 * p, 1090, 540 + 220 * p, 1102), LIME, 1, r=6)
        for i, s in enumerate(sub):
            p = eo(prog(t, 1.2 + i * 0.12)); text(fr, s, MED, 54, 540, 1200 + i * 74 + (1 - p) * 40, GREY, p, maxw=980)
        if chips:
            f = FT(SEM, 40); ws = [f.getlength(c) + 64 for c in chips]; x = 540 - (sum(ws) + 24 * (len(chips) - 1)) / 2
            for i, (c, w) in enumerate(zip(chips, ws)):
                p = eo(prog(t, 1.9 + i * 0.18, 0.45)); y = 1470 + (1 - p) * 60
                rrect(fr, (x, y - 42, x + w, y + 42), WHITE, 0.08 * p, r=42)
                rrect(fr, (x, y - 42, x + w, y + 42), WHITE, 0.35 * p, r=42, outline=3)
                text(fr, c, SEM, 40, x + w / 2, y, WHITE, p); x += w + 24
    ev = [(0.3, "impact", None), (0.3, "swish", None), (0.45, "swish", None), (0.8, "sweep", (0.6, 300, 900, 0.06))]
    ev += [(1.9 + i * 0.18, "pop", 1000 + i * 150) for i in range(len(chips or []))]
    return dur, fn, ev

def _marker(fr, kind, i, cx, cy, a):
    if kind == "num":
        circle(fr, cx, cy, 52, LIME, a); text(fr, str(i + 1), BLK, 60, cx, cy, DARK, a)
    elif kind == "x":
        circle(fr, cx, cy, 52, RED, a)
        polyline(fr, [(cx - 18, cy - 18), (cx + 18, cy + 18)], WHITE, a, 10); polyline(fr, [(cx + 18, cy - 18), (cx - 18, cy + 18)], WHITE, a, 10)
    else:
        circle(fr, cx, cy, 52, LIME, a); polyline(fr, [(cx - 22, cy + 2), (cx - 6, cy + 18), (cx + 22, cy - 16)], DARK, a, 10)

def T_list(head, items, marker="num", sub=None, dur=5.0, start=0.6, step=0.6, footnote=None):
    n = len(items); y0 = 700 if sub else 650
    sp = min(200, (1640 - y0) / max(1, n - 1)) if n > 1 else 0
    def fn(fr, t):
        heading(fr, t, head, sub)
        for i, (a, b) in enumerate(items):
            p = eo(prog(t, start + i * step, 0.5)); y = y0 + i * sp; dx = (1 - p) * -80
            if p <= 0: continue
            _marker(fr, marker, i, 170 + dx, y, p)
            if b:
                text(fr, a, BLD, 58, 255 + dx, y - 22, WHITE, p, anchor="l", maxw=760)
                text(fr, b, MED, 36, 257 + dx, y + 38, GREY, p, anchor="l", maxw=760)
            else:
                text(fr, a, BLD, 58, 255 + dx, y, WHITE, p, anchor="l", maxw=760)
        foot(fr, t, footnote, start + n * step)
    kind = {"x": 260, "num": 800, "check": 1000}[marker]
    ev = [(start + i * step, "pop", kind + i * 90) for i in range(n)]
    if marker == "x": ev += [(start + i * step, "thud", None) for i in range(n)]
    return dur, fn, ev

def _valstr(v, k):
    if isinstance(v, str): return v
    num, dec, suf = v
    x = num * k
    return (fmt(x) if dec == 0 else f"{x:.{dec}f}".replace(".", ",")) + suf

def T_cards(head, cards, note=None, footnote=None, dur=4.6):
    n = len(cards); y0 = 680 if n == 3 else 760
    def fn(fr, t):
        heading(fr, t, head)
        for i, (acr, desc, val, vc) in enumerate(cards):
            st = 0.35 + i * 0.4; p = eo(prog(t, st, 0.55)); y = y0 + i * 300
            if p <= 0: continue
            dx = (1 - p) * 260
            rrect(fr, (80 + dx, y - 130, 1000 + dx, y + 130), CARD, 0.92 * p, r=40)
            rrect(fr, (80 + dx, y - 130, 1000 + dx, y + 130), WHITE, 0.08 * p, r=40, outline=2)
            rrect(fr, (80 + dx, y - 70, 92 + dx, y + 70), vc if vc != WHITE else LIME, p, r=6)
            text(fr, acr, BLK, 92, 140 + dx, y - 28, vc if vc != WHITE else WHITE, p, anchor="l", maxw=440)
            text(fr, desc, MED, 38, 142 + dx, y + 58, GREY, p, anchor="l", maxw=460)
            k = eo(prog(t, st + 0.15, 1.0))
            text(fr, _valstr(val, k), BLK, 80 if not isinstance(val, str) or len(val) < 7 else 56, 950 + dx, y - (10 if isinstance(val, str) else 0), vc, p, anchor="r", maxw=400)
        yn = y0 + (n - 1) * 300 + 220
        if note:
            p = eo(prog(t, 0.35 + n * 0.4 + 0.8)); text(fr, note, SEM, 44, 540, yn + (1 - p) * 40, LIME, p, maxw=980)
        foot(fr, t, footnote, 0.35 + n * 0.4 + 1.2)
    ev = []
    for i in range(n):
        c0 = 0.35 + i * 0.4
        ev += [(c0, "swish", None), (c0 + 0.05, "pop", 650 + i * 140)]
        if not isinstance(cards[i][2], str): ev += [(c0 + 0.2 + k * 0.13, "tick", None) for k in range(7)]
    if note: ev += [(0.35 + n * 0.4 + 0.8, "chime", None)]
    return dur, fn, ev

def T_vs(head, left, right, verdict, footnote=None, dur=6.0):
    rows = max(len(left["rows"]), len(right["rows"]))
    top = 580; bot = top + 150 + rows * 150
    def col(fr, t, d, x0, st, side):
        p = eo(prog(t, st, 0.55)); dx = (1 - p) * 200 * side
        if p <= 0: return
        rrect(fr, (x0 + dx, top, x0 + 450 + dx, bot), CARD, 0.92 * p, r=40)
        rrect(fr, (x0 + dx, top, x0 + 450 + dx, bot), d["color"], 0.6 * p, r=40, outline=3)
        text(fr, d["title"], BLK, 58, x0 + 225 + dx, top + 80, d["color"], p, maxw=390)
        for j, (lab, val) in enumerate(d["rows"]):
            pr = eo(prog(t, st + 0.35 + j * 0.25, 0.4)); y = top + 190 + j * 150
            text(fr, lab, MED, 32, x0 + 225 + dx, y - 26, GREY, p * pr, maxw=390)
            text(fr, val, BLK, 54, x0 + 225 + dx, y + 26, WHITE if j < len(d["rows"]) - 1 else d["color"], p * pr, maxw=400)
    def fn(fr, t):
        heading(fr, t, head)
        col(fr, t, left, 70, 0.4, -1); col(fr, t, right, 560, 0.9, 1)
        p = prog(t, 1.2, 0.4)
        if p > 0:
            circle(fr, 540, top + 80, 46 * eb(p), DARK, 1); circle(fr, 540, top + 80, 46 * eb(p), WHITE, 0.6, outline=3)
            text(fr, "VS", BLK, 34, 540, top + 80, WHITE, clamp(p * 2))
        vt = 0.9 + 0.35 + rows * 0.25 + 0.4
        for i, s in enumerate(verdict):
            p = eo(prog(t, vt + i * 0.15)); text(fr, s, SEM, 46, 540, bot + 90 + i * 66 + (1 - p) * 40, LIME, p, maxw=980)
        foot(fr, t, footnote, vt + 0.4)
    ev = [(0.4, "swish", None), (0.45, "pop", 600), (0.9, "swish", None), (0.95, "pop", 900), (1.2, "thud", None)]
    for j in range(rows): ev += [(0.75 + j * 0.25, "tick", None), (1.25 + j * 0.25, "tick", None)]
    ev += [(0.9 + 0.35 + rows * 0.25 + 0.4, "chime", None)]
    return dur, fn, ev

def T_formula(head, formula, rows, dur=4.6, footnote=None, sub=None):
    def fn(fr, t):
        heading(fr, t, head, sub)
        p = prog(t, 0.4, 0.5)
        if p > 0:
            s = 0.85 + 0.15 * eb(p); a = clamp(p * 2)
            rrect(fr, (540 - 460 * s, 720 - 100 * s, 540 + 460 * s, 720 + 100 * s), LIME, 0.12 * a, r=50)
            rrect(fr, (540 - 460 * s, 720 - 100 * s, 540 + 460 * s, 720 + 100 * s), LIME, a, r=50, outline=4)
            text(fr, formula, BLK, 76 * s, 540, 720, LIME, a, maxw=840)
        for i, (l, c, r) in enumerate(rows):
            st = 1.1 + i * 0.45; p = eo(prog(t, st, 0.5)); y = 960 + i * 170; dx = (1 - p) * 200
            if p <= 0: continue
            rrect(fr, (80 + dx, y - 70, 1000 + dx, y + 70), CARD, 0.92 * p, r=36)
            rrect(fr, (80 + dx, y - 70, 1000 + dx, y + 70), c, 0.5 * p, r=36, outline=2)
            text(fr, l, BLK, 54, 130 + dx, y, c, p, anchor="l", maxw=420)
            text(fr, r, SEM, 42, 950 + dx, y, WHITE, p, anchor="r", maxw=440)
        foot(fr, t, footnote, 1.1 + len(rows) * 0.45)
    ev = [(0.4, "impact", None), (0.45, "chime", None)] + [(1.1 + i * 0.45, "pop", 700 + i * 150) for i in range(len(rows))]
    return dur, fn, ev

def T_flow(head, nodes, footnote=None, dur=6.0, sub=None, step=0.75):
    n = len(nodes); y0 = 680 if sub else 640; sp = 250
    def fn(fr, t):
        heading(fr, t, head, sub)
        for i, (small, main, col) in enumerate(nodes):
            st = 0.5 + i * step; p = eo(prog(t, st, 0.5)); y = y0 + i * sp
            if i > 0:
                pa = eo(prog(t, st - 0.3, 0.3))
                if pa > 0:
                    yA = y - sp + 88; yB = yA + (sp - 176) * pa
                    polyline(fr, [(540, yA), (540, yB)], LIME, 0.9, 8)
                    if pa > 0.9: polygon(fr, [(522, yB - 6), (558, yB - 6), (540, yB + 14)], LIME, 0.9)
            if p <= 0: continue
            sc = 0.9 + 0.1 * p
            hw, hh = 430 * sc, 85 * sc
            last = i == n - 1
            rrect(fr, (540 - hw, y - hh, 540 + hw, y + hh), col if last else CARD, (1 if last else 0.92) * p, r=36)
            if not last: rrect(fr, (540 - hw, y - hh, 540 + hw, y + hh), col, 0.55 * p, r=36, outline=3)
            tc = DARK if last and col in (LIME, TEAL) else WHITE
            text(fr, small, SEM, 34, 540, y - 34, GREY if not last else tc, p, maxw=780)
            text(fr, main, BLK, 60, 540, y + 28, col if not last else tc, p, maxw=780)
        foot(fr, t, footnote, 0.5 + n * step)
    ev = []
    for i in range(n):
        st = 0.5 + i * step
        ev += [(st, "pop", 600 + i * 130)]
        if i: ev += [(st - 0.3, "sweep", (0.3, 400, 800, 0.05))]
    ev += [(0.5 + (n - 1) * step + 0.1, "chime", None)]
    return dur, fn, ev

def T_big(tag, num, suffix, subs, dur=4.0, dec=0):
    def fn(fr, t):
        p = eo(prog(t, 0.05)); text(fr, spaced(tag), SEM, 38, 540, 560 + (1 - p) * 40, LIME, p)
        pr = eo(prog(t, 0.3, 1.4))
        shape(fr, (310, 650, 771, 1111), WHITE, 0.12, lambda d, w, h: d.ellipse((0, 0, w - 1, h - 1), outline=255, width=14))
        if pr > 0: shape(fr, (310, 650, 771, 1111), LIME, 1, lambda d, w, h: d.arc((0, 0, w - 1, h - 1), start=-90, end=-90 + 360 * pr, fill=255, width=14))
        v = num * pr
        s = fmt(v) if dec == 0 else f"{v:.{dec}f}".replace(".", ",")
        text(fr, s, BLK, 260, 540, 880, LIME, eo(prog(t, 0.2, 0.3)), maxw=400)
        p = eo(prog(t, 1.5)); text(fr, suffix, BLK, 96, 540, 1220 + (1 - p) * 50, WHITE, p, maxw=980)
        for i, s2 in enumerate(subs):
            p = eo(prog(t, 1.8 + i * 0.15)); text(fr, s2, MED, 50, 540, 1340 + i * 70 + (1 - p) * 40, GREY, p, maxw=980)
    steps = max(1, int(num)) if dec == 0 else int(num * 10)
    steps = min(steps, 12)
    ev = [(0.3 + 1.4 * k / steps, "tick", None) for k in range(steps)] + [(1.7, "chime", None), (1.5, "swish", None)]
    return dur, fn, ev

def T_bars(head, rows, sub=None, footnote=None, dur=5.0, start=0.6, step=0.45):
    n = len(rows); mx = max(r[1] for r in rows); y0 = 720 if sub else 660
    sp = min(200, (1600 - y0) / max(1, n - 1))
    def fn(fr, t):
        heading(fr, t, head, sub)
        for i, (lab, val, disp, col) in enumerate(rows):
            st = start + i * step; p = eo(prog(t, st, 0.6)); y = y0 + i * sp
            if p <= 0: continue
            text(fr, lab, SEM, 42, 100, y - 42, WHITE, clamp(p * 1.5), anchor="l", maxw=700)
            rrect(fr, (100, y, 920, y + 58), WHITE, 0.07 * p, r=29)
            w = max(58, 820 * val / mx * p)
            rrect(fr, (100, y, 100 + w, y + 58), col, 1, r=29)
            text(fr, disp, BLK, 46, 980, y - 42, col, clamp(p * 1.5), anchor="r", maxw=300)
        foot(fr, t, footnote, start + n * step)
    ev = []
    for i in range(n): ev += [(start + i * step, "pop", 500 + i * 120), (start + i * step + 0.2, "tick", None)]
    return dur, fn, ev

def T_chartsteps(head, label, steps, dur=3.8):
    def fn(fr, t):
        p = eo(prog(t, 0.05)); text(fr, head, BLK, 100, 540, 410 + (1 - p) * 50, WHITE, p, maxw=980)
        text(fr, label, SEM, 42, 130, 560, LIME, eo(prog(t, 0.2, 0.4)), anchor="l")
        pts = partial(UP, eo(prog(t, 0.3, 1.3)))
        if len(pts) > 1:
            polygon(fr, pts + [(pts[-1][0], 1000), (pts[0][0], 1000)], LIME, 0.10)
            polyline(fr, pts, LIME, 1, 12); ex, ey = pts[-1]
            circle(fr, ex, ey, 34, LIME, 0.25); circle(fr, ex, ey, 15, LIME, 1)
        for i, (a, b) in enumerate(steps):
            st = 1.0 + i * 0.45; p = eo(prog(t, st, 0.5)); y = 1160 + i * 180; dx = (1 - p) * -80
            if p <= 0: continue
            _marker(fr, "num", i, 170 + dx, y, p)
            text(fr, a, BLD, 64, 255 + dx, y - 22, WHITE, p, anchor="l", maxw=760)
            text(fr, b, MED, 36, 257 + dx, y + 40, GREY, p, anchor="l", maxw=760)
    ev = [(0.3, "sweep", (1.3, 180, 720, 0.10)), (1.55, "pop", 1200)] + [(1.0 + i * 0.45, "pop", 800 + i * 200) for i in range(len(steps))]
    return dur, fn, ev

def T_cta(l1, l2, sub, button, sub2=None, dur=3.0):
    def fn(fr, t):
        p = eo(prog(t, 0.05)); text(fr, l1, BLK, 120, 540, 740 + (1 - p) * 60, WHITE, p, maxw=980)
        p = eo(prog(t, 0.25)); text(fr, l2, BLK, 120, 540, 885 + (1 - p) * 60, LIME, p, maxw=980)
        p = eo(prog(t, 0.6)); text(fr, sub, MED, 48, 540, 1050 + (1 - p) * 40, GREY, p, maxw=980)
        p = prog(t, 0.9, 0.5)
        if p > 0:
            s = 0.7 + 0.3 * eb(p); w, h = 680 * s, 136 * s
            if t > 1.4:
                rp = (t - 1.4) % 1.0; g = 1 + rp * 0.25
                rrect(fr, (540 - 340 * g, 1260 - 68 * g - rp * 20, 540 + 340 * g, 1260 + 68 * g + rp * 20), LIME, (1 - rp) * 0.6, r=90, outline=4)
            rrect(fr, (540 - w / 2, 1260 - h / 2, 540 + w / 2, 1260 + h / 2), LIME, clamp(p * 2), r=int(68 * s))
            text(fr, button, BLK, 58 * s, 540, 1260, DARK, clamp(p * 2), maxw=600 * s)
        if sub2: text(fr, sub2, MED, 40, 540, 1420, GREY, eo(prog(t, 1.3)) * 0.9, maxw=980)
    ev = [(0.05, "thud", None), (0.9, "impact_s", None), (0.95, "chime", None)]
    return dur, fn, ev

# ---------------- SFX ----------------
SR = 44100
RNG = np.random.default_rng(3)
def _pop(f):
    t = np.arange(int(0.12 * SR)) / SR
    return np.sin(2 * np.pi * (f * t + 300 * (1 - np.exp(-40 * t)) / 40)) * np.exp(-38 * t)
def _tick():
    t = np.arange(int(0.03 * SR)) / SR
    return np.diff(RNG.standard_normal(len(t)), prepend=0) * np.exp(-150 * t) * 0.5
def _whoosh(L=0.45, rise=True):
    n = int(L * SR); w = np.convolve(RNG.standard_normal(n), np.ones(5) / 5, mode="same")
    env = np.sin(np.linspace(0, np.pi, n)) ** 2
    if rise: env *= np.linspace(0.3, 1, n)
    return w * env
def _impact():
    t = np.arange(int(1.1 * SR)) / SR
    return np.sin(2 * np.pi * (40 * t + 60 * (1 - np.exp(-12 * t)) / 12)) * np.exp(-3.5 * t) + RNG.standard_normal(len(t)) * np.exp(-30 * t) * 0.35
def _sweep(L, f0, f1, g):
    t = np.arange(int(L * SR)) / SR; f = f0 * (f1 / f0) ** (t / L); ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) + 0.25 * np.sin(2 * ph)) * np.minimum(1, t / 0.05) * np.minimum(1, (L - t) / 0.15) * g
def _chime():
    t = np.arange(int(1.0 * SR)) / SR
    return sum(np.sin(2 * np.pi * f * t) * a for f, a in ((1046.5, .5), (1318.5, .35), (1568, .3))) * np.exp(-4 * t)
def _thud():
    t = np.arange(int(0.35 * SR)) / SR
    return np.sin(2 * np.pi * (70 * t + 80 * (1 - np.exp(-20 * t)) / 20)) * np.exp(-10 * t)

def _key():
    n = int(0.018 * SR); t = np.arange(n) / SR
    w = np.diff(RNG.standard_normal(n), prepend=0) * np.exp(-260 * t)
    body = np.sin(2 * np.pi * RNG.uniform(2100, 2600) * t) * np.exp(-400 * t) * 0.6
    return (w + body) * RNG.uniform(0.7, 1.0)
def _blip(f, L=0.07):
    t = np.arange(int(L * SR)) / SR
    sq = np.sign(np.sin(2 * np.pi * f * t)) * 0.35 + np.sin(2 * np.pi * f * t) * 0.65
    return sq * np.minimum(1, t / 0.003) * np.exp(-t / (L * 0.45))
def _riser(L=0.55):
    n = int(L * SR); t = np.arange(n) / SR
    nz = RNG.standard_normal(n); nz = nz - np.convolve(nz, np.ones(8) / 8, mode="same")
    f = 300 * (6 ** (t / L)); tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.35
    return (nz * 0.6 + tone) * (t / L) ** 2.2
def _sub(L=0.7):
    t = np.arange(int(L * SR)) / SR
    return np.sin(2 * np.pi * (48 * t + 90 * (1 - np.exp(-25 * t)) / 25)) * np.exp(-4.5 * t)
def _snap():
    n = int(0.05 * SR); t = np.arange(n) / SR
    return np.diff(RNG.standard_normal(n), prepend=0) * np.exp(-90 * t) * 0.9
def _glitch(L=0.25):
    n = int(L * SR); out = np.zeros(n); i = 0
    while i < n:
        seg = int(RNG.uniform(0.01, 0.04) * SR); e = min(n, i + seg)
        kind = RNG.integers(3); tt = np.arange(e - i) / SR
        if kind == 0: out[i:e] = RNG.standard_normal(e - i) * 0.5
        elif kind == 1: out[i:e] = np.sign(np.sin(2 * np.pi * RNG.uniform(300, 3000) * tt)) * 0.4
        i = e + int(RNG.uniform(0, 0.015) * SR)
    return out * np.linspace(1, 0.4, n)

def _swoosh(L=0.7):
    n = int(L * SR); t = np.arange(n) / SR
    nz = np.convolve(RNG.standard_normal(n), np.ones(30) / 30, mode="same") * 4
    env = np.exp(-((t - L * 0.55) / (L * 0.22)) ** 2)
    bass = np.sin(2 * np.pi * np.cumsum(140 * (0.45 ** (t / L))) / SR) * 0.5
    return (nz + bass) * env
def _data(L=0.35):
    n = int(L * SR); out = np.zeros(n); i = 0
    while i < n:
        seg = int(0.025 * SR); e = min(n, i + seg); tt = np.arange(e - i) / SR
        out[i:e] = np.sin(2 * np.pi * RNG.choice([7200, 8400, 9600]) * tt) * np.exp(-tt * 60) * 0.5
        i = e + int(0.012 * SR)
    return out

def make_audio(events, dur, path, style="classic"):
    if style == "ref": return make_audio_ref(events, dur, path)
    return _make_audio_classic(events, dur, path)

def make_audio_ref(events, dur, path):
    out = np.zeros(int(dur * SR) + 2 * SR)
    def add(t0, sig, g):
        s = int(t0 * SR)
        if 0 <= s < len(out): e = min(len(out), s + len(sig)); out[s:e] += sig[:e - s] * g
    for t0, k, prm in events:
        if k == "key": add(t0, _key(), 0.35)
        elif k == "tick": add(t0, _key(), 0.28)
        elif k == "pop": add(t0, _blip(700 + (prm or 800) * 0.5), 0.22)
        elif k == "swish":
            for j in range(4): add(t0 + j * 0.065, _key(), 0.3)
        elif k == "whoosh": add(t0 - 0.1, _riser(0.5), 0.16); add(t0 + 0.05, _swoosh(0.7), 0.55); add(t0 + 0.42, _snap(), 0.4)
        elif k == "impact": add(t0, _sub(0.9), 0.85); add(t0, _snap(), 0.45); add(t0 + 0.02, _glitch(0.22), 0.12)
        elif k == "impact_s": add(t0, _sub(0.6), 0.6); add(t0, _snap(), 0.3)
        elif k == "sweep":
            L = prm[0]; up = prm[2] > prm[1]; n = max(3, int(L / 0.09))
            for j in range(n):
                f = 600 + (j / (n - 1)) * 700 if up else 1300 - (j / (n - 1)) * 700
                add(t0 + j * L / n, _blip(f, 0.06), 0.13)
        elif k == "chime":
            for j, f in enumerate((880, 1175, 1568)): add(t0 + j * 0.07, _blip(f, 0.09), 0.2)
            add(t0 + 0.25, _data(0.3), 0.08)
        elif k == "thud": add(t0, _sub(0.45), 0.6); add(t0, _glitch(0.12), 0.1)
    out = out[:int(dur * SR)]
    out = np.tanh(out * 1.3); out = out / (np.max(np.abs(out)) + 1e-9) * 0.89
    data = (out * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.column_stack([data, data]).ravel().tobytes())

def _make_audio_classic(events, dur, path):
    out = np.zeros(int(dur * SR) + 2 * SR)
    def add(t0, sig, g):
        s = int(t0 * SR)
        if 0 <= s < len(out): e = min(len(out), s + len(sig)); out[s:e] += sig[:e - s] * g
    for t0, k, prm in events:
        if k == "key": add(t0, _tick(), 0.15)
        elif k == "pop": add(t0, _pop(prm), 0.45)
        elif k == "tick": add(t0, _tick(), 0.3 if prm is None else prm)
        elif k == "swish": add(t0, _whoosh(0.28, False), 0.09)
        elif k == "whoosh": add(t0, _whoosh(0.5), 0.22)
        elif k == "impact": add(t0, _impact(), 0.75)
        elif k == "impact_s": add(t0, _impact(), 0.4)
        elif k == "sweep": add(t0, _sweep(*prm[:3], prm[3]), 1)
        elif k == "chime": add(t0, _chime(), 0.35)
        elif k == "thud": add(t0, _thud(), 0.6)
    out = out[:int(dur * SR)]
    out = np.tanh(out * 1.2); out = out / (np.max(np.abs(out)) + 1e-9) * 0.89
    data = (out * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.column_stack([data, data]).ravel().tobytes())

# ---------------- video ----------------
class Video:
    def __init__(self, scenes):
        self.scenes = []; t = 0; self.events = []
        for dur, fn, ev in scenes:
            self.scenes.append((t, t + dur, fn))
            self.events += [(t + a, k, p) for a, k, p in ev]
            if t > 0: self.events.append((t - 0.42, "whoosh", None))
            t += dur
        self.dur = t

    def frame(self, t):
        global SA
        fr = background(t); n = len(self.scenes)
        for i, (a, b, fn) in enumerate(self.scenes):
            if a <= t < b or (i == n - 1 and t >= a):
                SA = (1 if i == 0 else clamp((t - a) / 0.18)) * (1 if i == n - 1 else clamp((b - t) / 0.18))
                fn(fr, t - a)
        SA = 1.0
        x0, x1, gap = 60, 1020, 12; sw = (x1 - x0 - gap * (n - 1)) / n
        for i, (a, b, _) in enumerate(self.scenes):
            sx = x0 + i * (sw + gap)
            rrect(fr, (sx, 64, sx + sw, 72), WHITE, 0.22, r=4)
            p = clamp((t - a) / (b - a))
            if p > 0: rrect(fr, (sx, 64, sx + max(8, sw * p), 72), WHITE, 0.95, r=4)
        return fr

    def stills(self):
        return [self.frame(b - 0.3) for a, b, _ in self.scenes]

    def render(self, out, style="classic"):
        wav = out[:-4] + ".wav"; make_audio(self.events, self.dur, wav, style)
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
               "-i", "-", "-i", wav, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium",
               "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for i in range(int(self.dur * FPS)): p.stdin.write(self.frame(i / FPS).tobytes())
        p.stdin.close(); p.wait(); os.remove(wav)
