from lib import *

CAPTION = "Reels reklamada matn ekranda juda tez almashsa, odam uni o'qishga ulgurmay keyingi videoga o'tib ketadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("EKRANDAGI MATN", [("Reels reklamangizda", WHITE, 92, 0), ("matn o'qiladimi?", GREY, 90, 0),
               ("Yoki tez o'tib ketadimi", LIME, 88, 1)], chart=("O'qilish", "↓")),
        T_vs("Bir xil matn", {"title": "1 SONIYA", "color": RED,
               "rows": [("O'qildi", "yarmi"), ("Tushunildi", "kam"), ("Arizalar", "8 ta")]},
             {"title": "2–3 SONIYA", "color": LIME,
               "rows": [("O'qildi", "to'liq"), ("Tushunildi", "aniq"), ("Arizalar", "17 ta")]},
             ["Matnga vaqt bering"], footnote=M, dur=6.2),
        T_list("Oddiy qoidalar", [("Qisqa yozing", "bir ekranda 5–7 so'z"),
               ("Vaqt bering", "har qatorga 2–3 soniya"),
               ("Katta shrift", "telefonda ham aniq ko'rinsin")], marker="check", dur=5.4),
        T_cta("Reklamangiz matnini", "birga tekshiramiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
