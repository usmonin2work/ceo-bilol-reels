from lib import *

CAPTION = "Reklamadan sotuvgacha mijoz bir necha qadamdan o'tadi va har bir qadamda uni yo'qotmaslik kerak."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("MIJOZ YO'LI", [("Reklamadan sotuvgacha", WHITE, 84, 0), ("nechta qadam bor?", GREY, 80, 0),
               ("har biri muhim", LIME, 110, 1)]),
        T_flow("Mijoz yo'li", [("1-qadam", "Reklamani ko'rdi", VIO), ("2-qadam", "Profilga kirdi", BLUE),
               ("3-qadam", "Direct'ga yozdi", TEAL), ("4-qadam", "Sotib oldi", LIME)], dur=6.0),
        T_bars("1000 ta ko'rishdan", [("Profilga kirdi", 100, "120", VIO), ("Direct'ga yozdi", 40, "45", BLUE),
               ("Suhbat bo'ldi", 25, "30", TEAL), ("Sotib oldi", 8, "9", RED)],
               sub="eng ko'p yo'qotilgan qadamni tuzatamiz", footnote=M, dur=5.0),
        T_cta("Mijoz yo'lingizni", "birga tekshiramiz.", SUB, BTN, "15 daqiqada zaif qadamni topamiz", dur=3.4),
    ]
