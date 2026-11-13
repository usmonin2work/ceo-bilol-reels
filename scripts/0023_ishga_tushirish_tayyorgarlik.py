from lib import *

CAPTION = "Reklamani yoqishdan oldin 5 ta narsa tayyor bo'lishi kerak."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("REKLAMANI YOQISHDAN OLDIN", [("Tayyorgarliksiz", WHITE, 100, 0), ("reklama", GREY, 90, 0),
               ("pulni yeydi", LIME, 130, 1)]),
        T_list("5 ta tayyorgarlik", [("Aniq taklif", "nima, kimga, qanchaga"), ("Kreativlar", "kamida 3 xil video"),
               ("Ariza joyi", "forma, bot yoki sayt"), ("Javob beruvchi", "lidga 5 daqiqada qo'ng'iroq"),
               ("Hisob-kitob", "lid va sotuv jadvalda")], marker="check", dur=6.0, step=0.55),
        T_vs("Natija farqi", {"title": "TAYYOR", "color": LIME,
               "rows": [("Lid narxi", "barqaror"), ("Javob", "5 daqiqada"), ("Sotuv", "o'lchanadi")]},
             {"title": "TAYYORSIZ", "color": RED,
               "rows": [("Lid narxi", "sakraydi"), ("Javob", "ertasiga"), ("Sotuv", "noma'lum")]},
             ["Avval tayyorlang, keyin yoqing"], footnote=M, dur=5.6),
        T_cta("Ishga tushirishni", "birga tekshiramiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
