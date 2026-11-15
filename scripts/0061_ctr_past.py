from lib import *

CAPTION = "CTR past bo'lsa, avval muammo kreativdami yoki auditoriyadami — shuni aniqlab oling."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("CTR NEGA PAST?", [("Reklamani ko'rishadi,", WHITE, 92, 0), ("lekin bosishmaydi", GREY, 92, 0),
               ("sabab qayerda?", LIME, 120, 1)], chart=("CTR", "↓")),
        T_vs("CTR 0.4% bo'lsa", {"title": "Kreativ", "color": ORANGE,
               "rows": [("Belgisi", "hamma joyda past"), ("Yechim", "yangi hook")]},
             {"title": "Auditoriya", "color": TEAL,
               "rows": [("Belgisi", "bir guruhda past"), ("Yechim", "auditoriyani toraytiring")]},
             ["bitta o'zgarishni sinang"], footnote=M, dur=6.0),
        T_list("Tekshirish tartibi", [("Ilk 3 soniya", "e'tiborni ushlayaptimi"), ("Taklif", "aniq va tushunarlimi"),
               ("Auditoriya", "kerakli odamlarmi")], marker="check", dur=4.8),
        T_cta("Kabinetingizni", "birga tekshiramiz.", SUB, BTN, "past CTR sababini topib beramiz", dur=3.4),
    ]
