from lib import *

CAPTION = "Kabinetingizdagi eng qimmatga tushayotgan bitta xatoni 15 daqiqalik auditda topib beramiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("15 DAQIQALIK AUDIT", [("Byudjetning katta qismi", WHITE, 86, 0), ("bitta xatoga", GREY, 92, 0),
               ("ketayotgan bo'lishi mumkin", LIME, 96, 1)], chart=("Byudjet", "↓")),
        T_bars("Oyiga 1000$ byudjetdan", [("Ishlayotgan qism", 55, "550$", TEAL),
               ("Noto'g'ri auditoriya", 25, "250$", ORANGE), ("Charchagan kreativ", 20, "200$", RED)],
               sub="bitta xato — butun oy uchun", footnote=M, dur=5.0),
        T_list("Auditda nimani ko'ramiz", [("Auditoriya", "kimga pul ketyapti"), ("Kreativ", "qaysi biri charchagan"),
               ("Natija", "qaysi biri sotuv beryapti")], marker="check", dur=4.6),
        T_cta("Eng qimmat xatoni", "birga topamiz.", SUB, BTN, "15 daqiqada aniq ko'rsatamiz", dur=3.4),
    ]
