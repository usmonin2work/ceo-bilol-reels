from lib import *

CAPTION = "Do'kondagi sotuvni ham CRM orqali reklamaga qaytaring."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("SOTUV DO'KONDA BO'LSA-CHI?", [("Mijoz reklamani ko'rdi,", WHITE, 90, 0), ("lekin do'konda oldi", GREY, 90, 0),
               ("reklama buni bilmaydi", LIME, 115, 1)]),
        T_flow("Sotuvni reklamaga qaytaramiz", [("Reklama", "lid keladi", VIO), ("CRM", "lid yoziladi", BLUE),
               ("Do'kon", "sotuv belgilanadi", TEAL), ("Reklama", "sotuvni o'rganadi", LIME)], dur=6.0),
        T_vs("Natija farqi", {"title": "CRM BILAN", "color": LIME,
               "rows": [("Optimizatsiya", "sotuvga"), ("Auditoriya", "xaridorlar"), ("Hisob", "aniq")]},
             {"title": "CRMSIZ", "color": RED,
               "rows": [("Optimizatsiya", "arizaga"), ("Auditoriya", "tasodifiy"), ("Hisob", "taxminiy")]},
             ["Reklama nimani o'lchasa, shuni ko'paytiradi"], footnote=M, dur=5.6),
        T_cta("Offline sotuvni", "reklamaga ulaymiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
