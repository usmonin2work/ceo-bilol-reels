from lib import *

CAPTION = "Biz bilan ishlashning birinchi 30 kunida haftama-hafta nimalar o'zgaradi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("30 KUNLIK REJA", [("Reklamadan natija", WHITE, 100, 0), ("qachon chiqadi?", GREY, 90, 0),
               ("Haftama-hafta", LIME, 130, 1)]),
        T_flow("Birinchi 30 kun", [("1-hafta", "Audit va sozlash", VIO), ("2-hafta", "Kreativ testlari", BLUE),
               ("3-hafta", "Yutganini kuchaytirish", TEAL), ("4-hafta", "Barqaror arizalar", LIME)], dur=6.0),
        T_bars("Ariza narxi, haftalar", [("1-hafta", 100, "100%", RED), ("2-hafta", 80, "80%", BLUE),
               ("3-hafta", 62, "62%", TEAL), ("4-hafta", 50, "50%", LIME)],
               sub="test qilib, arzonlashtiramiz", footnote=M, dur=5.0),
        T_cta("Sizning 30 kunlik", "rejangizni tuzamiz.", SUB, BTN, "15 daqiqada kabinetni ko'rib chiqamiz", dur=3.4),
    ]
