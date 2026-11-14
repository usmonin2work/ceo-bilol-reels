from lib import *

CAPTION = "Reklamangiz birdan to'xtab qolsa, sababini 24 soat ichida topib, qayta ishga tushiramiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, holat har bir kabinetda farq qiladi"

def scenes():
    return [
        T_hook("REKLAMA TO'XTADI", [("Kecha arizalar bor edi.", WHITE, 90, 0), ("Bugun — nol.", GREY, 100, 0),
               ("Sabab bor", LIME, 130, 1)]),
        T_list("Eng ko'p uchraydigan sabablar", [("Rad etilgan e'lon", "qoidaga zid matn yoki rasm"),
               ("To'lov muammosi", "karta yoki limit tugagan"),
               ("Kreativ charchagan", "bir xil odamlarga qayta-qayta")], marker="num", dur=5.2),
        T_flow("24 soatlik tekshiruv", [("1-soat", "Kabinet va to'lovni ko'ramiz", WHITE),
               ("6-soat", "E'lon va auditoriya tahlili", BLUE), ("24-soat", "Tuzatib, qayta yoqamiz", LIME)],
               footnote=M, dur=5.4),
        T_cta("Reklamangizni", "qayta yurgizamiz.", SUB, BTN, "15 daqiqada kabinetni ko'rib chiqamiz", dur=3.4),
    ]
