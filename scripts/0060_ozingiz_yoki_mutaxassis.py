from lib import *

CAPTION = "Reklamani o'zingiz yuritasizmi yoki mutaxassisga berasizmi — asosiy farq vaqt va arizaning narxida."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("O'ZINGIZMI YOKI MUTAXASSIS?", [("Reklamani kim", WHITE, 96, 0), ("yuritishi", GREY, 92, 0),
               ("natijani o'zgartiradi", LIME, 100, 1)], chart=("Ariza narxi", "↓")),
        T_vs("Oyiga 500$ byudjetda", {"title": "O'zingiz", "color": ORANGE,
               "rows": [("Haftalik vaqt", "8–10 soat"), ("Ariza narxi", "5$")]},
             {"title": "Mutaxassis", "color": TEAL,
               "rows": [("Haftalik vaqt", "1 soat"), ("Ariza narxi", "2.5$")]},
             ["vaqtingiz biznesga qoladi"], footnote=M, dur=6.0),
        T_list("Qachon o'zingiz yuritsangiz bo'ladi", [("Kichik byudjet", "sinov bosqichida"), ("Vaqtingiz bor", "har kuni kuzata olsangiz"),
               ("O'rganishga tayyor", "xatolarga pul to'lab")], marker="check", dur=4.8),
        T_cta("Kabinetingizni", "birga ko'rib chiqamiz.", SUB, BTN, "qaysi yo'l sizga mosligini aytamiz", dur=3.4),
    ]
