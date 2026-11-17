from lib import *

CAPTION = "Bitta reklamaga ko'p xabar tiqilsa, odam hech birini eslab qolmaydi, shuning uchun har reklamada bitta g'oya bo'lsin."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("BITTA G'OYA", [("Reklamada hammasini", WHITE, 96, 0), ("aytmoqchimisiz?", GREY, 90, 0),
               ("Odam hech birini eslamaydi", LIME, 84, 1)], chart=("Eslab qolish", "↓")),
        T_vs("Bir xil byudjet", {"title": "5 XABAR", "color": RED,
               "rows": [("Xabarlar", "chegirma, yetkazish..."), ("Eslab qoladi", "kam"), ("Arizalar", "12 ta")]},
             {"title": "1 G'OYA", "color": LIME,
               "rows": [("Xabar", "bitta aniq foyda"), ("Eslab qoladi", "ko'p"), ("Arizalar", "27 ta")]},
             ["Aniq xabar — ko'proq ariza"], footnote=M, dur=6.2),
        T_list("Qanday qilish kerak", [("Bitta muammo", "mijozning eng katta og'rig'i"),
               ("Bitta yechim", "sizning asosiy foydangiz"),
               ("Bitta harakat", "nima qilishini aniq ayting")], marker="check", dur=5.4),
        T_cta("Reklama xabaringizni", "birga tekshiramiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
