from lib import *

CAPTION = "Bitta kampaniyada reklama juda ko'p bo'lsa, byudjet bo'linib ketadi va hech biri yaxshi ishlamaydi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("15 TA REKLAMA?", [("Bitta kampaniyada", WHITE, 92, 0), ("15 ta reklama", GREY, 90, 0),
               ("bu xato", LIME, 130, 1)], chart=("Natija", "↓")),
        T_vs("Bir xil byudjet, kuniga", {"title": "15 ta", "color": RED,
               "rows": [("Har biriga", "~7 000"), ("O'rganish", "tugamaydi"), ("Natija", "tarqoq")]},
             {"title": "3–4 ta", "color": TEAL,
               "rows": [("Har biriga", "~30 000"), ("O'rganish", "tez"), ("Natija", "barqaror")]},
             ["kam reklama — aniq natija"], footnote=M, dur=6.0),
        T_list("To'g'ri tartib", [("3–4 ta", "kreativ bilan boshlang"),
               ("Kuzating", "3–5 kunda yaxshisini aniqlang"),
               ("Almashtiring", "kuchsizini o'chirib, yangisini qo'shing")], marker="num", dur=5.4),
        T_cta("Kampaniyangiz tuzilishini", "tekshirib beramiz.", SUB, BTN, "byudjet qayerga bo'linayotganini ko'rasiz", dur=3.4),
    ]
