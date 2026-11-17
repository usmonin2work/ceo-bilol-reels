from lib import *

CAPTION = "Reklamangiz pulni qaysi auditoriyaga sarflayotganini bepul auditda aniq ko'rsatib beramiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("PULINGIZ KIMGA KETYAPTI?", [("Reklama ishlayapti,", WHITE, 100, 0), ("lekin kimga", GREY, 90, 0),
               ("ko'rsatilyapti?", LIME, 120, 1)], chart=("Byudjet", "?")),
        T_bars("1 000 000 so'm byudjetdan", [("Mos auditoriya", 35, "35%", LIME), ("Juda keng", 30, "30%", BLUE),
               ("Mos emas", 20, "20%", ORANGE), ("Tasodifiy klik", 15, "15%", RED)],
               sub="ko'p qismi sotib olmaydiganlarga", footnote=M, dur=5.0),
        T_list("Auditda ko'rsatamiz", [("Kim ko'ryapti", "yosh, joy, qiziqishlar"),
               ("Kim ariza qoldiryapti", "qaysi auditoriya pul olib keladi"),
               ("Nimani o'chirish kerak", "befoyda sarfni to'xtatamiz")], marker="check", dur=5.0),
        T_cta("Auditoriyangizni", "birga tekshiramiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
