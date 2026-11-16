from lib import *

CAPTION = "Mijoz e'tirozlariga reklama matnining o'zida oldindan javob bersangiz, Direct'da savol kamayib, ariza ko'payadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("E'TIROZLAR", [("Mijoz o'ylaydi:", WHITE, 96, 0), ("«qimmat-ku»", GREY, 90, 0),
               ("javob bering", LIME, 130, 1)], chart=("Ariza", "↓")),
        T_vs("Bir xil taklif, boshqa matn", {"title": "Oddiy", "color": RED,
               "rows": [("Matn", "faqat taklif"), ("Savol", "narx? kafolat?"), ("Natija", "o'ylab ko'raman")]},
             {"title": "Javobli", "color": TEAL,
               "rows": [("Matn", "taklif + javob"), ("Savol", "oldindan yopilgan"), ("Natija", "ariza qoldiradi")]},
             ["Direct'da savol kamayadi"], footnote=M, dur=6.0),
        T_list("Matnda javob bering", [("Narx", "nima uchun shu narx turadi"),
               ("Ishonch", "kafolat yoki natija misoli"),
               ("Vaqt", "qancha vaqtda natija bo'ladi")], marker="num", dur=5.4),
        T_cta("Reklama matningizni", "tekshirib beramiz.", SUB, BTN, "qaysi e'tiroz arizani to'xtatayotganini ko'rasiz", dur=3.4),
    ]
