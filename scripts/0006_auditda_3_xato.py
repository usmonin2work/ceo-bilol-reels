from lib import *

CAPTION = "Bepul auditda deyarli har bir kabinetda topadigan 3 ta xato."
SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"

def scenes():
    return [
        T_hook("BEPUL AUDITDAN", [("Har bir", WHITE, 120, 0), ("kabinetda", WHITE, 110, 0),
               ("shu 3 xato", LIME, 150, 1)]),
        T_list("Eng ko'p uchraydigan", [("Maqsad — klik", "sotuv uchun emas, arzon klik uchun"),
               ("Kreativ yangilanmaydi", "bir video oylab aylanadi"), ("Natija o'lchanmaydi", "lid sotuvga bog'lanmagan")],
               marker="x", dur=5.2, step=0.8),
        T_flow("Auditdan keyin", [("15 daqiqa", "Kabinetni ko'ramiz", WHITE), ("Natija", "Xatolar ro'yxati", BLUE),
               ("Sizda qoladi", "Aniq reja", LIME)], dur=5.0),
        T_cta("Kabinetingizni", "tekshirib beramiz.", SUB, BTN, "bepul, majburiyatsiz", dur=3.4),
    ]
