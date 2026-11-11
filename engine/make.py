"""Render one Reels video from a script file.

Usage (from repo root):
    python3 engine/make.py scripts/0001_mavzu.py            # renders videos/0001_mavzu.mp4
    python3 engine/make.py scripts/0001_mavzu.py --stills   # saves videos/0001_mavzu_preview.png (check before rendering)

A script file defines  scenes()  returning a list of templates from engine/lib.py
(T_hook, T_title, T_list, T_cards, T_vs, T_formula, T_flow, T_big, T_bars, T_chartsteps, T_cta)
and a one-line CAPTION string. See scripts/_example.py.
"""
import sys, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib, sfx_pro
from PIL import Image

lib.make_audio = lambda ev, dur, path, style=None: sfx_pro.make(ev, dur, path)

def load(path):
    spec = importlib.util.spec_from_file_location("script", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

if __name__ == "__main__":
    path = sys.argv[1]; name = os.path.splitext(os.path.basename(path))[0]
    root = os.path.dirname(HERE); out_dir = os.path.join(root, "videos"); os.makedirs(out_dir, exist_ok=True)
    m = load(path); v = lib.Video(m.scenes())
    if "--stills" in sys.argv:
        ims = [im.resize((270, 480)) for im in v.stills()]
        c = Image.new("RGB", (270 * len(ims), 480))
        for i, im in enumerate(ims): c.paste(im, (i * 270, 0))
        c.save(os.path.join(out_dir, f"{name}_preview.png")); print("preview saved")
    else:
        tmp = os.path.join(out_dir, f"{name}.tmp.mp4"); final = os.path.join(out_dir, f"{name}.mp4")
        v.render(tmp); os.replace(tmp, final); print(final, round(v.dur, 1), "s")
