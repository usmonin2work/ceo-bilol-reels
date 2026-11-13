from lib import *

CAPTION = "Landing sahifangiz 5 soniyada nimani taklif qilishini aytib bera oladimi?"

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("5 SONIYA TESTI", [("Sahifangizga", WHITE, 100, 0), ("kirgan odam", GREY, 90, 0),
               ("5 soniyada ketadi", LIME, 120, 1)]),
        T_list("5 soniyada tushunarli bo'lsin", [("Nima?", "nima sotyapsiz"),
               ("Kimga?", "kim uchun foydali"), ("Keyin nima?", "qaysi tugmani bosish")],
               marker="check", dur=4.8),
        T_bars("100 ta tashrifdan ariza", [("Chalkash sahifa", 30, "2", RED), ("Aniq sahifa", 100, "7", TEAL)],
               sub="birinchi ekran hammasini hal qiladi", footnote=M, dur=5.0),
        T_cta("Sahifangizni", "birga tekshiramiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
