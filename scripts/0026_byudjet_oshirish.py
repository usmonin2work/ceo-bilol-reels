from lib import *

CAPTION = "Byudjetni oshirganda CAC o'sib ketmasligi uchun uni bosqichma-bosqich ko'taring."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("BYUDJETNI 3 BAROBAR OSHIRDINGIZMI?", [("Sotuv", WHITE, 100, 0), ("emas,", GREY, 90, 0),
               ("CAC o'sdi", LIME, 120, 1)]),
        T_bars("Keskin oshirilganda CAC", [("$20/kun", 40, "$12", TEAL), ("$40/kun", 55, "$16", BLUE),
               ("$60/kun", 100, "$29", RED)],
               sub="algoritm qayta o'rganishga tushadi", footnote=M, dur=5.0),
        T_list("To'g'ri masshtab", [("Qadam", "byudjetni 20% dan oshirmang"),
               ("Vaqt", "har 3 kunda bir marta ko'taring"), ("Kreativ", "yangi variantlarni oldindan tayyorlang")],
               marker="check", dur=4.8),
        T_cta("Byudjetni oshirishni", "birga rejalashtiramiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
