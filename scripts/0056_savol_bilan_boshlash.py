from lib import *

CAPTION = "Reklamani to'g'ri savol bilan boshlasangiz, tomoshabin javobni bilish uchun oxirigacha ko'radi."

def scenes():
    return [
        T_hook("SAVOLLI HOOK", [("Birinchi 2 soniya", WHITE, 92, 0), ("savol bo'lsa,", GREY, 88, 0),
               ("odam to'xtaydi", LIME, 124, 1)]),
        T_vs("Bir xil mahsulot, ikki xil boshlanish",
             {"title": "Oddiy", "color": ORANGE, "rows": [("Boshlanish", "biz eng zo'r"), ("Tomoshabin", "o'tkazadi")]},
             {"title": "Savolli", "color": TEAL, "rows": [("Boshlanish", "nega sotilmaydi?"), ("Tomoshabin", "o'ylaydi")]},
             ["Savol javobni", "kutishga majburlaydi"], dur=5.6),
        T_list("Yaxshi savol qanday bo'ladi", [("Mijoz og'rig'idan", "uning tilida"),
               ("Qisqa va aniq", "bir qatorda"), ("Javob videoda", "oxirigacha ushlaydi")],
               marker="check", dur=4.8),
        T_cta("Savol bilan boshlang,", "e'tiborni ushlang.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying",
              "va do'stingizga ulashing"),
    ]
