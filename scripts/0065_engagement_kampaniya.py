from lib import *

CAPTION = "Layk va izoh ko'p bo'lsa ham, Engagement kampaniyasi ariza va sotuv uchun mo'ljallanmagan."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("LAYK KO'P, SOTUV YO'Q?", [("Layklar oshdi,", WHITE, 100, 0), ("kassa esa", GREY, 90, 0),
               ("bo'sh qoldi", LIME, 130, 1)], chart=("Sotuvlar", "↓")),
        T_vs("Bir xil 1 mln so'm byudjet", {"title": "Engagement", "color": RED,
               "rows": [("Layk", "1 200 ta"), ("Ariza", "3 ta"), ("Sotuv", "0 ta")]},
             {"title": "Lid / Xabar", "color": TEAL,
               "rows": [("Layk", "150 ta"), ("Ariza", "40 ta"), ("Sotuv", "6 ta")]},
             ["algoritm siz so'ragan natijani beradi"], footnote=M, dur=6.0),
        T_list("Engagement qachon foydasiz", [("Maqsad — ariza", "u layk bosuvchilarni topadi"),
               ("Kichik byudjet", "pul 'chiroyli' raqamga ketadi"),
               ("Hisobot — layk", "sotuv esa ko'rinmaydi")], marker="num", dur=5.0),
        T_cta("Kampaniya maqsadini", "birga to'g'rilaymiz.", SUB, BTN, "byudjet sotuvga ishlasin", dur=3.4),
    ]
