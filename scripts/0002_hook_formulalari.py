from lib import *

CAPTION = "Reklamangizni birinchi 3 soniyada to'xtatib ko'radigan 4 xil boshlanish."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("BIRINCHI 3 SONIYA", [("Odam reklamani", WHITE, 100, 0), ("3 soniyada", GREY, 90, 0),
               ("o'tkazib yuboradi", LIME, 120, 1)]),
        T_list("4 ta hook formulasi", [("Savol", "«Lid ko'p, sotuv yo'qmi?»"),
               ("Raqam", "«100 ta lid — 8 ta sotuv»"),
               ("Xato", "«Bu xatoni 90% qiladi»"),
               ("Natija", "«30 kunda arizalar 2x»")], marker="num", dur=5.4),
        T_bars("3 soniyada qolganlar", [("Umumiy boshlanish", 22, "22%", RED), ("Savol bilan", 38, "38%", BLUE),
               ("Raqam bilan", 45, "45%", TEAL), ("Og'riq nuqtasi", 52, "52%", LIME)],
               sub="1000 ta ko'rishdan", footnote=M, dur=5.0),
        T_cta("Hook'ingizni", "birga tekshiramiz.", SUB, BTN, "15 daqiqada kreativlarni ko'rib chiqamiz", dur=3.4),
    ]
