from lib import *

CAPTION = "Reklamani yoqishdan oldin profilingizni tayyorlang — mijoz avval bio va highlights'ga qaraydi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija soha va taklifga bog'liq"

def scenes():
    return [
        T_hook("REKLAMADAN OLDIN", [("Mijoz reklamani", WHITE, 95, 0), ("ko'rgach, profilga", GREY, 90, 0),
               ("kiradi", LIME, 130, 1)]),
        T_bars("100 ta profilga kirgandan", [("Profilni ko'rdi", 100, "100", VIO), ("Bio'ni o'qidi", 70, "70", BLUE),
               ("Highlights'ni ochdi", 40, "40", TEAL), ("Direct'ga yozdi", 6, "6", RED)],
               sub="profil tayyor bo'lmasa, odam chiqib ketadi", footnote=M, dur=5.0),
        T_list("Profilda 3 ta narsa bo'lsin", [("Bio", "kimga, nima, qanday foyda"),
               ("Highlights", "narxlar, natijalar, savollar"),
               ("Aloqa", "Direct yoki tugma aniq")], marker="check", dur=5.0),
        T_cta("Profilingizni", "birga tekshiramiz.", SUB, BTN, "15 daqiqada kamchiliklarni ko'rsatamiz", dur=3.4),
    ]
