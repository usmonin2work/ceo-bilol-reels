from lib import *

CAPTION = "Sohangizda bitta mijoz qanchaga tushishi kerakligini auditda hisoblaymiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("CAC QANCHA BO'LISHI KERAK?", [("Bitta mijoz", WHITE, 100, 0), ("sizga", GREY, 90, 0),
               ("qanchaga tushyapti?", LIME, 110, 1)]),
        T_bars("Bitta mijoz narxi", [("Reklama xarajati", 100, "$500", VIO), ("Lidlar", 50, "50 ta", BLUE),
               ("Sotuvlar", 20, "10 ta", TEAL), ("CAC", 30, "$50", RED)],
               sub="CAC = xarajat ÷ sotuvlar", footnote=M, dur=5.0),
        T_list("Auditda hisoblaymiz", [("Joriy CAC", "hozir mijoz qanchaga tushadi"),
               ("Chegara", "foyda qolishi uchun maksimum"), ("Reja", "CAC ni qanday tushirish")],
               marker="check", dur=4.6),
        T_cta("Sizning CAC ni", "birga hisoblaymiz.", SUB, BTN, "15 daqiqada aniq raqam", dur=3.4),
    ]
