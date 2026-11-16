from lib import *

CAPTION = "Lid narxi oshib ketsa, byudjetni o'zgartirishdan oldin kreativ, auditoriya va taklifni tekshiring."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("LID QIMMATLADI?", [("Lid narxi", WHITE, 100, 0), ("birdan oshdi", GREY, 90, 0),
               ("vahima qilmang", LIME, 120, 1)]),
        T_bars("Lid narxi, haftalar bo'yicha", [("1-hafta", 40, "20 000", TEAL), ("2-hafta", 55, "27 000", BLUE),
               ("3-hafta", 80, "39 000", VIO), ("4-hafta", 100, "48 000", RED)],
               sub="sababini topmasdan byudjetni tegmang", footnote=M, dur=5.0),
        T_list("Birinchi 3 joy", [("Kreativ", "eskirdimi, chastota oshdimi"),
               ("Auditoriya", "torayib qoldimi, kesishyaptimi"),
               ("Taklif", "raqobatchidan kuchsizmi")], marker="num", dur=5.4),
        T_cta("Lid narxingizni", "birga tushiramiz.", SUB, BTN, "15 daqiqada sababini ko'rsatamiz", dur=3.4),
    ]
