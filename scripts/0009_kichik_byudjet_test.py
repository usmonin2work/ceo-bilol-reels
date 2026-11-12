from lib import *

CAPTION = "Kichik byudjet bilan ham boshlash mumkin — muhimi, to'g'ri test rejasi."
SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("KICHIK BYUDJET", [("Oz pul bilan", WHITE, 110, 0), ("boshlasa", GREY, 90, 0),
               ("bo'ladimi?", LIME, 140, 1)]),
        T_flow("Minimal test rejasi", [("1-hafta", "3 ta kreativ, 1 auditoriya", WHITE),
               ("2-hafta", "Eng yaxshisini qoldiramiz", BLUE), ("3-hafta", "Byudjetni asta oshiramiz", LIME)],
               footnote=M, dur=5.4),
        T_list("Pulni tejaydigan qoidalar", [("Bitta maqsad", "faqat lid yoki sotuv"),
               ("Kam, lekin aniq", "2–3 kreativ yetarli"), ("Har kuni o'lchang", "lid narxini kuzating")],
               marker="check", dur=4.8),
        T_cta("Byudjetingizga mos", "reja tuzib beramiz.", SUB, BTN, "bepul, majburiyatsiz", dur=3.4),
    ]
