from lib import *

CAPTION = "Reklamani har gal to'xtatib qayta yoqsangiz, algoritm o'rganishni boshidan boshlaydi va ariza narxi oshib ketadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("TO'XTATIB, QAYTA YOQISH", [("Reklamani o'chirib", WHITE, 92, 0), ("yana yoqdingizmi?", GREY, 90, 0),
               ("natija buziladi", LIME, 120, 1)], chart=("Natija", "↓")),
        T_flow("Nima bo'ladi?", [("1-qadam", "Reklama to'xtadi", RED),
               ("2-qadam", "O'rganish yo'qoldi", ORANGE),
               ("3-qadam", "Qaytadan sinov", BLUE),
               ("natija", "Ariza qimmatladi", LIME)], footnote=M, dur=6.0),
        T_list("To'g'ri yo'l", [("Kuting", "kamida 3–5 kun tegmang"),
               ("Yangi kreativ", "eskisini o'chirmasdan qo'shing"),
               ("Byudjet", "asta-sekin o'zgartiring")], marker="check", dur=5.4),
        T_cta("Reklamangizni", "birga tekshiramiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
