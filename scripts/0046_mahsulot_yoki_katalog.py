from lib import *

CAPTION = "Butun katalogni emas, avval eng ko'p sotiladigan bitta mahsulotni reklama qiling."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija soha va byudjetga bog'liq"

def scenes():
    return [
        T_hook("NIMANI REKLAMA QILISH?", [("Bitta mahsulot", WHITE, 100, 0), ("yoki butun katalog?", GREY, 95, 0),
               ("Avval bittasi", LIME, 125, 1)]),
        T_vs("Kichik byudjetda",
             {"title": "Katalog", "color": BLUE, "rows": [("Byudjet", "bo'linadi"), ("Xabar", "tarqoq"), ("Natija", "sekin")]},
             {"title": "Bitta xit", "color": LIME, "rows": [("Byudjet", "jamlanadi"), ("Xabar", "aniq"), ("Natija", "tezroq")]},
             ["Avval bitta xit,", "keyin katalog"], footnote=M, dur=6.0),
        T_list("Qachon katalogga o'tish kerak", [("Xit mahsulot", "barqaror sotilsa"),
               ("Byudjet", "kuniga yetarli bo'lsa"),
               ("Retarget", "ko'rganlarga katalog")], marker="check", dur=5.0),
        T_cta("To'g'ri mahsulotni", "birga tanlaymiz.", SUB, BTN, "15 daqiqada kabinetni ko'rib chiqamiz", dur=3.4),
    ]
