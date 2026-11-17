from lib import *

CAPTION = "Biznesingiz uchun bitta lidga qancha to'lash foydali ekanini sotuvdan orqaga qarab hisoblaymiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("LID NARXI", [("Bitta lid uchun", WHITE, 92, 0), ("qancha to'lash mumkin?", GREY, 80, 0),
               ("sotuvdan hisoblaymiz", LIME, 96, 1)]),
        T_formula("Maqsadli lid narxi", "Foyda × Konversiya", [("Bitta sotuv foydasi", LIME, "500 000 so'm"),
                  ("Liddan sotuvga", BLUE, "10%"), ("Maksimal lid narxi", ORANGE, "50 000 so'm")],
                  footnote=M, dur=5.4),
        T_list("Keyin nima qilamiz", [("Lid narxi pastroq", "reklamani kengaytiramiz"),
               ("Lid narxi yuqoriroq", "taklif va auditoriyani tuzatamiz"),
               ("Konversiya past", "sotuv bo'limini tekshiramiz")], marker="check", dur=5.0),
        T_cta("Lid narxingizni", "birga hisoblaymiz.", SUB, BTN, "15 daqiqada aniq raqam chiqaramiz", dur=3.4),
    ]
