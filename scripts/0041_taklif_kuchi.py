from lib import *

CAPTION = "Reklamani kuchaytirishdan oldin taklifingizni kuchaytiring — aks holda byudjet bekorga ketadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("TAKLIF KUCHI", [("Reklama yaxshi.", WHITE, 100, 0), ("Lekin sotuv yo'q.", GREY, 90, 0),
               ("Muammo — taklifda", LIME, 120, 1)]),
        T_vs("Bir xil reklama", {"title": "ODDIY", "color": RED,
               "rows": [("Taklif", "Kurs sotiladi"), ("Lid narxi", "$4"), ("Sotuv", "kam")]},
             {"title": "KUCHLI", "color": LIME,
               "rows": [("Taklif", "+bonus, kafolat"), ("Lid narxi", "$1.5"), ("Sotuv", "ko'p")]},
             ["Odam reklamani emas, taklifni sotib oladi"], footnote=M, dur=6.0),
        T_list("Taklifni kuchaytiring", [("Aniq natija", "nima olishini ayting"),
               ("Bonus", "qo'shimcha qiymat bering"),
               ("Kafolat", "xavfni kamaytiring")], marker="check", dur=4.8),
        T_cta("Taklifingizni birga", "kuchaytiramiz.", SUB, BTN, "15 daqiqada kabinetni ko'rib chiqamiz", dur=3.4),
    ]
