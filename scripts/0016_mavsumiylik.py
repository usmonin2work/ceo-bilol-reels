from lib import *

CAPTION = "Bayram aksiyasi uchun reklamani kamida 3 hafta oldin tayyorlash kerak."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, muddat soha va byudjetga bog'liq"

def scenes():
    return [
        T_hook("BAYRAM YAQINLASHYAPTI", [("Reklamani", WHITE, 110, 0), ("bayram kuni boshlash", GREY, 80, 0),
               ("kech qolish", LIME, 130, 1)]),
        T_flow("Aksiyaga tayyorlanish", [("3 hafta oldin", "Kreativ va oferta", VIO),
               ("2 hafta oldin", "Test va o'rganish", BLUE), ("1 hafta oldin", "Byudjetni oshirish", TEAL),
               ("Bayram", "Retargeting va sotuv", LIME)], footnote=M, dur=6.0),
        T_list("Oldindan tayyorlang", [("Kreativlar", "3–5 ta variant"), ("Oferta", "muddatli, aniq chegirma"),
               ("Auditoriya", "oldingi mijozlar ro'yxati")], marker="check", dur=4.8),
        T_cta("Bayram kampaniyangizni", "birga rejalaymiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
