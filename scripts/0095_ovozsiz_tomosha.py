from lib import *

CAPTION = "Reklamangizni ovozsiz ko'rib chiqing: rasm va ekrandagi matndan gap tushunilmasa, uni qayta ishlash kerak."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"

def scenes():
    return [
        T_hook("OVOZSIZ TOMOSHA", [("Reklamangiz", WHITE, 96, 0), ("ovozsiz ham", GREY, 90, 0),
               ("tushunarlimi?", LIME, 116, 1)], chart=("Tushunish", "↓")),
        T_vs("Ovoz o'chiq bo'lsa", {"title": "Yomon", "color": RED, "rows": [("Boshlanish", "Gapiruvchi yuz"), ("Ma'no", "Faqat ovozda"), ("Natija", "Skip")]},
             {"title": "Yaxshi", "color": LIME, "rows": [("Boshlanish", "Katta matn"), ("Ma'no", "Rasmda ko'rinadi"), ("Natija", "Ariza")]},
             ["Gapni ko'z bilan ham ayting"], dur=6.0),
        T_list("Tekshirish usuli", [("Ovozni o'chiring", "videoni boshidan ko'ring"),
               ("Matn", "har asosiy fikr ekranda"),
               ("Harakat", "mahsulotni ko'rsating")], marker="check", dur=5.2),
        T_cta("Reklamangizni", "birga tekshiramiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
