from lib import *

CAPTION = "Reklama kabineti va sahifa doim sizning nomingizda bo'lishi kerak."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"

def scenes():
    return [
        T_hook("KABINET KIMNING NOMIDA?", [("Targetolog ketdi,", WHITE, 100, 0), ("kabinet ham", GREY, 90, 0),
               ("u bilan ketdi", LIME, 130, 1)]),
        T_vs("Kabinet egasi",
             {"title": "Begona", "color": RED, "rows": [("Statistika", "yo'qoladi"), ("Pixel", "qaytadan"), ("Nazorat", "yo'q")]},
             {"title": "Sizniki", "color": LIME, "rows": [("Statistika", "saqlanadi"), ("Pixel", "o'qiydi"), ("Nazorat", "to'liq")]},
             ["Ma'lumot —", "biznesingiz boyligi"], dur=6.0),
        T_list("Biz qanday ishlaymiz", [("Kabinet", "sizning nomingizda ochiladi"),
               ("Kirish", "bizga faqat ruxsat beriladi"), ("To'lov", "kartangizdan, to'g'ridan-to'g'ri")],
               marker="check", dur=4.8),
        T_cta("Kabinetingizni", "birga tekshiramiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
