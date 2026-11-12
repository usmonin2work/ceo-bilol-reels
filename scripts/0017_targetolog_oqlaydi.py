from lib import *

CAPTION = "Targetolog xarajati sotuvdan kelgan foyda bilan o'lchanadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("TARGETOLOG KERAKMI?", [("Xizmat narxi", WHITE, 110, 0), ("emas, undan", GREY, 90, 0),
               ("keladigan foyda", LIME, 130, 1)]),
        T_vs("Bir oylik hisob",
             {"title": "O'zingiz", "color": ORANGE, "rows": [("Byudjet", "5 mln"), ("Sotuv", "10 ta"), ("Foyda", "3 mln")]},
             {"title": "Targetolog", "color": LIME, "rows": [("Byudjet + xizmat", "7 mln"), ("Sotuv", "25 ta"), ("Foyda", "8 mln")]},
             ["Xarajat emas,", "foydaning o'sishini solishtiring"], footnote=M, dur=6.4),
        T_list("Qachon o'zini oqlaydi", [("Mahsulot", "foydasi xizmat narxini yopadi"),
               ("Byudjet", "oyiga kamida test uchun yetadi"), ("Sotuv", "lidlarga tez javob beriladi")],
               marker="check", dur=4.8),
        T_cta("Sizda o'zini oqlaydimi?", "birga hisoblaymiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
