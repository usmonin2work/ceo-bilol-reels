from lib import *

CAPTION = "Reklama oxirida «batafsil» emas, odam aynan nima qilishi kerakligini aniq yozsangiz, ariza ko'payadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("ANIQ CTA", [("Reklama oxirida", WHITE, 96, 0), ("«Batafsil» deysizmi?", GREY, 90, 0),
               ("Odam nima qilishni bilmaydi", LIME, 84, 1)], chart=("Arizalar", "↓")),
        T_vs("Bir xil reklama", {"title": "«BATAFSIL»", "color": RED,
               "rows": [("Harakat", "noaniq"), ("Bosganlar", "ko'p emas"), ("Arizalar", "9 ta")]},
             {"title": "ANIQ HARAKAT", "color": LIME,
               "rows": [("Harakat", "«NARX» deb yozing"), ("Bosganlar", "ko'proq"), ("Arizalar", "21 ta")]},
             ["Aniq so'z — ko'proq ariza"], footnote=M, dur=6.2),
        T_list("Yaxshi CTA qanday", [("Bitta fe'l", "yozing, qo'ng'iroq qiling, band qiling"),
               ("Aniq joy", "Direct, sayt yoki telefon"),
               ("Sabab", "nima oladi: narx, audit, chegirma")], marker="check", dur=5.4),
        T_cta("Reklamangiz CTA'sini", "birga tekshiramiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
