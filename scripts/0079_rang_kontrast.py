from lib import *

CAPTION = "Reklamadagi rang va kontrast lentada ko'zni to'xtatadi, shuning uchun kreativni telefonda kichik holatda tekshiramiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("RANG VA KONTRAST", [("Reklamangiz", WHITE, 92, 0), ("lentada ko'rinmayaptimi?", GREY, 76, 0),
               ("sabab — rang", LIME, 110, 1)], chart=("To'xtash", "↓")),
        T_vs("Bir xil taklif, lentada", {"title": "Xira", "color": RED,
               "rows": [("Fon", "kulrang"), ("Matn", "och, mayda"), ("CTR", "~0,6%")]},
             {"title": "Kontrast", "color": TEAL,
               "rows": [("Fon", "to'q, toza"), ("Matn", "yorqin, yirik"), ("CTR", "~1,4%")]},
             ["ko'z birinchi kontrastni ko'radi"], footnote=M, dur=6.0),
        T_list("Tez tekshiruv", [("1 ta asosiy rang", "brendga mos, yorqin"),
               ("Matn", "fonga qarshi aniq o'qiladi"),
               ("Telefonda", "kichik holatda ham ko'rinadi")], marker="check", dur=5.4),
        T_cta("Kreativlaringizni", "tekshirib beramiz.", SUB, BTN, "lentada ajralib turishini ko'rasiz", dur=3.4),
    ]
