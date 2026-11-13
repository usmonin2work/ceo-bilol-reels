from lib import *

CAPTION = "Toshkent va viloyatlar uchun reklamani alohida kampaniyalarga ajrating."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("BUTUN O'ZBEKISTONGA BITTA REKLAMA?", [("Byudjet", WHITE, 100, 0), ("Toshkentga", GREY, 90, 0),
               ("yeb ketiladi", LIME, 120, 1)]),
        T_bars("Bitta kampaniyada byudjet", [("Toshkent", 70, "70%", VIO), ("Samarqand", 12, "12%", BLUE),
               ("Farg'ona", 10, "10%", TEAL), ("Boshqa viloyatlar", 8, "8%", RED)],
               sub="algoritm arzon ko'rsatuvga qarab ketadi", footnote=M, dur=5.0),
        T_list("Alohida kampaniya beradi", [("Byudjet", "har hududga aniq taqsimlanadi"),
               ("Kreativ", "hudud tili va narxiga mos"), ("Hisob", "qaysi viloyat sotishini ko'rasiz")],
               marker="check", dur=4.8),
        T_cta("Hududlar bo'yicha", "reklamani sozlaymiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
