from lib import *

CAPTION = "Sharh va keyslar reklamaga ishonchni oshirib, lid narxini tushiradi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija soha va kreativga bog'liq"

def scenes():
    return [
        T_hook("IJTIMOIY ISBOT", [("Mijozlar", WHITE, 110, 0), ("sizga emas,", GREY, 90, 0),
               ("boshqalarga ishonadi", LIME, 100, 1)]),
        T_bars("Lid narxi", [("Oddiy kreativ", 100, "$4.0", RED), ("Sharh bilan", 75, "$3.0", BLUE),
               ("Video keys bilan", 55, "$2.2", TEAL)],
               sub="Ishonch oshsa, lid arzonlashadi", footnote=M, dur=5.0),
        T_list("Nimani ko'rsatish kerak", [("Real sharh", "skrinshot yoki ovozli xabar"),
               ("Keys", "oldin va keyin raqamlar"), ("Mijoz videosi", "telefonda, oddiy tilda")],
               marker="check", dur=4.8),
        T_cta("Keyslaringizni", "reklamaga aylantiramiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
