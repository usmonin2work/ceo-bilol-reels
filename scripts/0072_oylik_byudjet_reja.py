from lib import *

CAPTION = "Reklama byudjetini kunma-kun emas, oylik reja asosida bosqichlarga bo'lib taqsimlaymiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("BYUDJET REJASI", [("Pulni har kuni", WHITE, 92, 0), ("tavakkal sarflaysizmi?", GREY, 80, 0),
               ("oylik reja kerak", LIME, 115, 1)]),
        T_bars("Oylik byudjet, haftalar bo'yicha", [("1-hafta: test", 20, "20%", BLUE),
               ("2-hafta: tahlil", 25, "25%", VIO), ("3-hafta: kuchaytirish", 30, "30%", TEAL),
               ("4-hafta: masshtab", 25, "25%", LIME)],
               sub="yutgan reklamaga ko'proq pul", footnote=M, dur=5.2),
        T_list("Reja nima beradi", [("Nazorat", "pul qayerga ketgani aniq"),
               ("Tezlik", "yutqazgan reklama erta to'xtaydi"),
               ("Natija", "byudjet ishlaydiganiga o'tadi")], marker="check", dur=5.0),
        T_cta("Byudjetingiz uchun", "oylik reja tuzamiz.", SUB, BTN, "15 daqiqada taqsimotni ko'rsatamiz", dur=3.4),
    ]
