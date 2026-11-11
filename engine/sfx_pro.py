"""Layered stereo SFX: filtered-noise whooshes, sub impacts, mechanical keys, bell chimes, shared reverb."""
import wave
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve

SR = 44100
R = np.random.default_rng(11)

def _sos(kind, f, order=2):
    return butter(order, np.array(f) / (SR / 2), kind, output="sos")
def lp(x, f, o=2): return sosfilt(_sos("low", f, o), x)
def hp(x, f, o=2): return sosfilt(_sos("high", f, o), x)
def bp(x, lo, hi, o=2): return sosfilt(_sos("band", [lo, hi], o), x)

def pink(n):
    X = np.fft.rfft(R.standard_normal(n)); f = np.arange(len(X)); f[0] = 1
    y = np.fft.irfft(X / np.sqrt(f), n)
    return y / (np.abs(y).max() + 1e-9)

def svf_bp(x, fc, q):
    """Band-pass with a moving centre frequency (Chamberlin state-variable filter)."""
    low = band = 0.0; out = [0.0] * len(x); xs = x.tolist()
    fs = (2 * np.sin(np.pi * np.minimum(fc, SR / 6.5) / SR)).tolist(); d = 1.0 / q
    for i in range(len(xs)):
        low += fs[i] * band
        high = xs[i] - low - d * band
        band += fs[i] * high
        out[i] = band
    return np.array(out)

def pan(x, p):
    """p in [-1, 1] (scalar or per-sample) -> stereo, equal power."""
    a = (np.asarray(p) + 1) * np.pi / 4
    return np.column_stack([x * np.cos(a), x * np.sin(a)])

def fade(x, a=0.003, r=0.01):
    n = len(x); na, nr = int(a * SR), int(r * SR)
    e = np.ones(n); e[:na] = np.linspace(0, 1, na); e[n - nr:] *= np.linspace(1, 0, nr)
    return x * e

# ---------- sounds (each returns stereo, peak ~1) ----------
def whoosh(L=0.62, lo=280, hi=4200, direction=1):
    n = int(L * SR); t = np.arange(n) / L / SR
    pk = 0.58
    env = np.where(t < pk, (t / pk) ** 2.6, ((1 - t) / (1 - pk)) ** 1.8)
    fc = lo * (hi / lo) ** np.where(t < pk, t / pk, 1 - 0.55 * (t - pk) / (1 - pk))
    body = svf_bp(pink(n) * 3 + R.standard_normal(n) * 0.5, fc, 1.6)
    air = hp(R.standard_normal(n), 5000) * 0.10 * env ** 1.5
    low = lp(pink(n), 180) * 2.2 * env
    x = fade(body * env + air + low * 0.5, 0.02, 0.05)
    st = pan(x, direction * (t * 1.6 - 0.8))
    return st / np.abs(st).max()

def swish(L=0.24):
    return whoosh(L, 900, 6500, R.choice([-1, 1])) * 1.0

def impact(big=True):
    L = 1.3 if big else 0.8; n = int(L * SR); t = np.arange(n) / SR
    f = 36 + 70 * np.exp(-t * 26)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * (3.2 if big else 5.5))
    punch = np.sin(2 * np.pi * np.cumsum(60 + 160 * np.exp(-t * 60)) / SR) * np.exp(-t * 22)
    click = lp(R.standard_normal(n), 7000) * np.exp(-t * 420)
    tail = bp(R.standard_normal(n), 180, 2400) * np.exp(-t * 9) * 0.22
    x = np.tanh((sub * 1.0 + punch * 0.7) * 1.6) + click * 0.5 + tail
    st = np.column_stack([fade(x + tail * 0.3, 0.0005, 0.08), fade(x + np.roll(tail, 300) * 0.3, 0.0005, 0.08)])
    return st / np.abs(st).max()

def thud():
    n = int(0.42 * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(46 + 80 * np.exp(-t * 34)) / SR) * np.exp(-t * 11)
    x += lp(R.standard_normal(n), 900) * np.exp(-t * 70) * 0.5
    x = fade(np.tanh(x * 1.4), 0.001, 0.05)
    return np.column_stack([x, x]) / np.abs(x).max()

def pop(freq=800.0):
    """Soft UI 'bubble': quick upward pitch bend, short decay, a breath of noise at the onset."""
    base = 330 + (freq - 500) * 0.38
    n = int(0.11 * SR); t = np.arange(n) / SR
    f = base * (1 + 0.9 * (1 - np.exp(-t * 55)))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 42)
    x += 0.28 * np.sin(4 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 70)
    x += bp(R.standard_normal(n), 1500, 5000) * np.exp(-t * 300) * 0.25
    x = fade(x, 0.002, 0.02)
    return pan(x, R.uniform(-0.25, 0.25)) / np.abs(x).max()

def key():
    """Mechanical key: bright click + short wooden 'thock'."""
    n = int(0.07 * SR); t = np.arange(n) / SR
    click = bp(R.standard_normal(n), 1800, 6500) * np.exp(-t * R.uniform(480, 700))
    f1, f2 = R.uniform(170, 230), R.uniform(380, 520)
    thock = (np.sin(2 * np.pi * f1 * t) + 0.6 * np.sin(2 * np.pi * f2 * t)) * np.exp(-t * 85)
    up = np.zeros(n); k = int(R.uniform(0.028, 0.04) * SR)
    up[k:] = (bp(R.standard_normal(n - k), 2500, 7000) * np.exp(-t[:n - k] * 800)) * 0.35
    x = fade(click * 0.9 + thock * 0.55 + up, 0.0005, 0.01) * R.uniform(0.75, 1.0)
    return pan(x, R.uniform(-0.35, 0.35)) / 1.6

def count_tick():
    n = int(0.03 * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * R.uniform(2300, 2700) * t) * np.exp(-t * 260) + bp(R.standard_normal(n), 3000, 8000) * np.exp(-t * 600) * 0.4
    return pan(fade(x, 0.0005, 0.005), R.uniform(-0.2, 0.2))

def bell(f, L=1.4):
    n = int(L * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for ratio, amp, dec in ((1, 1, 3.2), (2.0, .45, 4.5), (2.76, .32, 6), (5.4, .16, 9), (8.93, .07, 14)):
        x += amp * np.sin(2 * np.pi * f * ratio * t + R.uniform(0, 6.28)) * np.exp(-t * dec)
    x += bp(R.standard_normal(n), 3000, 9000) * np.exp(-t * 180) * 0.15
    return fade(x, 0.002, 0.1)

def chime():
    """Two-note 'success' bell (perfect fifth up)."""
    a, b = bell(987.77), bell(1479.98)
    n = len(a) + int(0.11 * SR); st = np.zeros((n, 2))
    st[:len(a)] += pan(a, -0.25); st[n - len(b):] += pan(b, 0.25) * 0.85
    return st / np.abs(st).max()

def shimmer(L, up=True):
    """Soft tonal glide for a line being drawn."""
    n = int(L * SR); t = np.arange(n) / SR; u = t / L
    f0, f1 = (320, 880) if up else (700, 240)
    f = f0 * (f1 / f0) ** u
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = (np.sin(ph) + 0.35 * np.sin(2.01 * ph)) * (0.7 + 0.3 * np.sin(2 * np.pi * 9 * t))
    x += svf_bp(pink(n) * 2, f * 3, 3.0) * 0.6
    x = fade(x * np.sin(np.pi * u) ** 0.7, 0.05, 0.15)
    return pan(x, (u * 1.2 - 0.6) * (1 if up else -1)) / np.abs(x).max()

def riser(L=0.5):
    n = int(L * SR); u = np.arange(n) / n
    x = svf_bp(R.standard_normal(n), 600 * (9 ** u), 2.5) * u ** 3
    x = fade(x, 0.02, 0.004)
    return np.column_stack([x, x]) / np.abs(x).max()

_IR = None
def reverb_ir():
    global _IR
    if _IR is None:
        n = int(1.1 * SR); t = np.arange(n) / SR
        ir = np.column_stack([bp(R.standard_normal(n), 250, 6500), bp(R.standard_normal(n), 250, 6500)]) * np.exp(-t * 6.5)[:, None]
        ir[: int(0.012 * SR)] = 0
        _IR = ir / np.sqrt((ir ** 2).sum(0)).mean()
    return _IR

# gain, reverb send
MIX = {"whoosh": (0.50, 0.25), "swish": (0.16, 0.2), "impact": (0.95, 0.30), "impact_s": (0.70, 0.25), "thud": (0.60, 0.12),
       "pop": (0.34, 0.22), "key": (0.30, 0.10), "tick": (0.10, 0.05), "chime": (0.26, 0.55), "sweep": (0.11, 0.35), "riser": (0.14, 0.3)}

def make(events, dur, path):
    n = int(dur * SR); dry = np.zeros((n + 3 * SR, 2)); wet = np.zeros_like(dry)
    def add(t0, sig, kind, g=1.0):
        s = int(t0 * SR)
        if s < 0: sig = sig[-s:]; s = 0
        if s >= len(dry): return
        e = min(len(dry), s + len(sig)); gain, send = MIX[kind]
        dry[s:e] += sig[:e - s] * gain * g; wet[s:e] += sig[:e - s] * gain * g * send
    wdir = 1
    for t0, k, prm in sorted(events, key=lambda e: e[0]):
        if k == "key": add(t0, key(), "key")
        elif k == "tick": add(t0, count_tick(), "tick")
        elif k == "pop": add(t0, pop(prm or 800), "pop")
        elif k == "swish": add(t0 - 0.06, swish(), "swish")
        elif k == "whoosh":
            # peak of the whoosh lands exactly on the cut (cut is at t0 + 0.42)
            w = whoosh(0.66, direction=wdir); wdir = -wdir
            add(t0 + 0.42 - 0.58 * 0.66, w, "whoosh"); add(t0 - 0.08, riser(0.5), "riser"); add(t0 + 0.42, thud(), "thud", 0.45)
        elif k == "impact": add(t0, impact(True), "impact")
        elif k == "impact_s": add(t0, impact(False), "impact_s")
        elif k == "thud": add(t0, thud(), "thud")
        elif k == "chime": add(t0, chime(), "chime")
        elif k == "sweep": add(t0, shimmer(prm[0], prm[2] > prm[1]), "sweep")
    rv = np.column_stack([fftconvolve(wet[:, c], reverb_ir()[:, c])[: len(dry)] for c in (0, 1)])
    mix = (dry + rv * 0.5)[:n]
    mix[:, 0] = hp(mix[:, 0], 28); mix[:, 1] = hp(mix[:, 1], 28)
    k = int(0.25 * SR); mix[-k:] *= np.linspace(1, 0, k)[:, None]
    mix = np.tanh(mix * 1.15)
    mix = mix / (np.abs(mix).max() + 1e-9) * 0.9
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
    return mix
