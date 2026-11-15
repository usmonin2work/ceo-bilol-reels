from lib import *

CAPTION = "Reklama va sotuv bo'limini alohida emas, bitta voronka sifatida birga ko'rib chiqamiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("REKLAMAMI YOKI SOTUVMI?", [("Marketolog sotuvchini,", WHITE, 92, 0), ("sotuvchi marketologni", GREY, 84, 0),
               ("ayblayapti", LIME, 130, 1)]),
        T_vs("100 ta arizadan 5 ta sotuv",
             {"title": "Marketolog", "color": BLUE, "rows": [("Fikri", "lid yetarli"), ("Aybdor", "sotuvchi")]},
             {"title": "Sotuvchi", "color": ORANGE, "rows": [("Fikri", "lid sifatsiz"), ("Aybdor", "reklama")]},
             ["Javob bahsda emas,", "raqamlarda"], footnote=M, dur=5.6),
        T_flow("Bitta zanjir sifatida", [("1. Reklama", "Kim keldi?", VIO), ("2. Ariza", "Qancha va qachon?", BLUE),
               ("3. Javob", "Necha daqiqada?", TEAL), ("4. Sotuv", "Nega olmadi?", LIME)], dur=5.6),
        T_cta("Reklama va sotuvni", "birga tekshiramiz.", SUB, BTN, "Uzilish qayerdaligini ko'rsatamiz", dur=3.4),
    ]
