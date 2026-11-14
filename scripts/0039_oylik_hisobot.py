from lib import *

CAPTION = "Oylik hisobotda sizga faqat biznesingiz uchun muhim 3 ta raqamni ko'rsatamiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("HISOBOT TUSHUNARLIMI?", [("Hisobotda 50 ta", WHITE, 100, 0), ("raqam bor, lekin", GREY, 90, 0),
               ("foyda ko'rinmaydi", LIME, 120, 1)]),
        T_cards("Biz ko'rsatadigan 3 raqam", [("Lid", "bitta ariza narxi", "25 000", TEAL),
               ("Sotuv", "bitta mijoz narxi", "180 000", BLUE), ("Daromad", "har 1 so'mga qaytgan", "x4", LIME)],
               footnote=M, dur=5.4),
        T_list("Har oy shuni bilasiz", [("Nima ishladi", "qaysi reklama sotdi"), ("Nima o'chdi", "pul qayerda isrof bo'ldi"),
               ("Keyingi qadam", "kelasi oy rejasi")], marker="check", dur=5.0),
        T_cta("Raqamlaringizni", "birga ko'ramiz.", SUB, BTN, "15 daqiqada kabinetingizni tahlil qilamiz", dur=3.4),
    ]
