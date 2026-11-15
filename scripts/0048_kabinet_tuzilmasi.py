from lib import *

CAPTION = "Tartibsiz reklama kabinetini aniq tuzilmaga keltirsak, byudjet qayerga ketayotgani ko'rinadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, har bir kabinet har xil"

def scenes():
    return [
        T_hook("KABINETINGIZ QANDAY?", [("20 ta kampaniya,", WHITE, 95, 0), ("hech biri", GREY, 90, 0),
               ("tushunarsiz", LIME, 130, 1)], chart=("Natija", "↓")),
        T_vs("Bizdan oldin va keyin",
             {"title": "Oldin", "color": RED, "rows": [("Kampaniya", "20 ta, nomsiz"), ("Byudjet", "hammasiga oz-oz")]},
             {"title": "Keyin", "color": BLUE, "rows": [("Kampaniya", "3 ta, aniq nom"), ("Byudjet", "eng yaxshisiga")]},
             ["Tuzilma aniq bo'lsa,", "pul qayerga ketgani ko'rinadi"], footnote=M, dur=6.0),
        T_list("Biz 3 qatlam quramiz", [("Sovuq", "yangi auditoriya, sinov"),
               ("Iliq", "qiziqqanlarga retarget"),
               ("Issiq", "ariza qoldirganlarga taklif")], marker="check", dur=5.0),
        T_cta("Kabinetingizni", "birga tartiblaymiz.", SUB, BTN, "15 daqiqada tuzilmani ko'rsatamiz", dur=3.4),
    ]
