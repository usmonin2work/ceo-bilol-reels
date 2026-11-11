import sys, os
from PIL import Image
import lib, sfx_pro
from lib import *

lib.make_audio = lambda ev, dur, path, style=None: sfx_pro.make(ev, dur, path)
SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def p1():
    return [
        T_hook("MIJOZ QAYERDA YO'QOLYAPTI?", [("Reklama ishlayapti,", WHITE, 100, 0), ("mijoz esa", GREY, 90, 0),
               ("yo'lda yo'qolyapti", LIME, 130, 1)], chart=("Sotuvlar", "↓")),
        T_bars("100 ta arizadan", [("Ariza qoldirdi", 100, "100", VIO), ("Vaqtida javob oldi", 60, "60", BLUE),
               ("Suhbat bo'ldi", 35, "35", TEAL), ("Sotib oldi", 8, "8", RED)],
               sub="har bosqichda odam yo'qoladi", footnote=M, dur=5.0),
        T_list("Biz 3 joyni tuzatamiz", [("Reklama", "to'g'ri odamga, to'g'ri taklif"), ("Sahifa", "klik arizaga aylansin"),
               ("Sotuv bilan aloqa", "lid sovib qolmasin")], marker="check", dur=4.6),
        T_cta("Voronkangizni", "birga tekshiramiz.", SUB, BTN, "15 daqiqada teshiklarni ko'rsatamiz", dur=3.4),
    ]

def p2():
    return [
        T_hook("TARGETOLOG YOLLASHDAN OLDIN", [("Targetologga", WHITE, 120, 0), ("shu 3 savolni", WHITE, 100, 0),
               ("bering", LIME, 170, 1)]),
        T_list("3 ta savol", [("Natijani nimada o'lchaysiz?", "klikdami yoki sotuvda?"),
               ("Kabinet kimning nomida?", "ma'lumotlar sizda qoladimi?"),
               ("Hisobot qachon va qanday?", "har hafta, raqamlar bilan?")], dur=5.2, step=0.8),
        T_vs("Javoblarni solishtiring",
             {"title": "Xavfli javob", "color": RED, "rows": [("Natija", "qamrov, layk"), ("Kabinet", "meniki"), ("Hisobot", "so'rasangiz")]},
             {"title": "Bizning javob", "color": LIME, "rows": [("Natija", "CAC va sotuv"), ("Kabinet", "sizniki"), ("Hisobot", "har dushanba")]},
             ["To'g'ri javob —", "doim raqamlarda"], dur=6.0),
        T_cta("Savollaringizga", "javob beramiz.", SUB, BTN, "bepul audit bilan boshlaymiz", dur=3.4),
    ]

def p3():
    return [
        T_hook("HALOL GAP", [("«100% kafolat»", WHITE, 110, 0), ("deganlarga", GREY, 90, 0), ("ishonmang", LIME, 160, 1)]),
        T_title("BIZ BERADIGAN NARSA", "TO'LIQ", "SHAFFOFLIK", ["Va'da emas — har hafta", "tekshirsa bo'ladigan raqamlar"]),
        T_list("Biz nimani va'da qilamiz", [("Kabinet sizning nomingizda", "barcha ma'lumot sizda qoladi"),
               ("Har hafta hisobot", "CPQL, CAC, ROAS"), ("Har bir so'm ko'rinadi", "byudjet qayerga ketgani"),
               ("Aniq reja", "keyingi hafta nima qilamiz")], marker="check", dur=5.4),
        T_cta("Va'da emas,", "raqamlar.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]

VIDEOS = [("P1_mijoz_qayerda_yoqolyapti", p1), ("P2_targetologga_3_savol", p2), ("P3_shaffoflik", p3)]

if __name__ == "__main__":
    os.makedirs("out", exist_ok=True)
    if sys.argv[1] == "stills":
        rows = [[im.resize((270, 480)) for im in Video(f()).stills()] for _, f in VIDEOS]
        c = Image.new("RGB", (270 * 4, 480 * len(rows)), (40, 40, 40))
        for j, r in enumerate(rows):
            for i, im in enumerate(r): c.paste(im, (i * 270, j * 480))
        c.save("out/grid_p.png")
        Video(p1()).stills()[1].save("out/full_p1.png")
    elif sys.argv[1] == "audio":
        for name, f in VIDEOS:
            v = Video(f()); m = sfx_pro.make(v.events, v.dur, f"out/{name}.wav")
            import numpy as np
            print(name, round(v.dur, 1), "rms", round(float(np.sqrt((m ** 2).mean())), 3), "peak", round(float(abs(m).max()), 2))
    else:
        name, f = VIDEOS[int(sys.argv[1])]
        v = Video(f()); v.render(f"out/{name}.mp4"); print(name, round(v.dur, 1))
