from lib import *

CAPTION = "Reels reklamada video uzunligini taxmin bilan emas, 15, 30 va 60 soniyani sinab ko'rib tanlaymiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("VIDEO UZUNLIGI", [("15, 30 yoki 60", WHITE, 92, 0), ("soniya?", GREY, 80, 0),
               ("qaysi biri yaxshi", LIME, 105, 1)]),
        T_cards("Har birining vazifasi", [("15 s", "bitta g'oya, tez", "ko'rish", LIME),
               ("30 s", "muammo + yechim", "ariza", TEAL),
               ("60 s", "batafsil tushuntirish", "ishonch", VIO)], dur=5.0),
        T_bars("Bitta ariza narxi, uzunlik bo'yicha", [("15 soniya", 60, "60 000", BLUE),
               ("30 soniya", 42, "42 000", LIME), ("60 soniya", 75, "75 000", VIO)],
               sub="uchalasini bir vaqtda sinang", footnote=M, dur=5.0),
        T_cta("Reklamangiz uchun", "qaysi uzunlik ishlaydi?", SUB, BTN, "15 daqiqada tahlil qilib beramiz", dur=3.4),
    ]
