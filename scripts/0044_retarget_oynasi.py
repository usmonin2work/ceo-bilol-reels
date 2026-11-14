from lib import *

CAPTION = "Retargetda 7, 30 va 180 kunlik auditoriyaga bir xil reklama ko'rsatish — pulni sovurish."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar soha va byudjetga bog'liq"

def scenes():
    return [
        T_hook("RETARGET OYNASI", [("Saytga kirgan hamma", WHITE, 90, 0), ("bir xil emas.", GREY, 100, 0),
               ("7, 30 yoki 180 kun?", LIME, 120, 1)]),
        T_cards("Oyna bo'yicha issiqlik", [("7 kun", "hali eslaydi", "x3", LIME),
               ("30 kun", "o'ylab yuribdi", "x1.5", BLUE), ("180 kun", "deyarli unutgan", "x1", GREY)],
               footnote=M, dur=5.4),
        T_list("Har biriga o'z xabari", [("7 kun", "chegirma yoki tezkor taklif"),
               ("30 kun", "sharh va natijalar"),
               ("180 kun", "yangi mahsulot bilan eslatma")], marker="check", dur=5.0),
        T_cta("Retargetingni", "to'g'ri bo'lamiz.", SUB, BTN, "15 daqiqada kabinetni ko'rib chiqamiz", dur=3.4),
    ]
