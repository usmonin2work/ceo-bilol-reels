from lib import *

CAPTION = "Birinchi 7 kunda reklama kabinetida nimalarni sozlashimizni qisqacha ko'rsatamiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, tartib biznesingizga qarab o'zgaradi"

def scenes():
    return [
        T_hook("BIRINCHI 7 KUN", [("Reklama natijasi", WHITE, 100, 0), ("birinchi haftada", GREY, 90, 0),
               ("qo'yilgan poydevordan", LIME, 100, 1)]),
        T_flow("1-haftalik reja", [("1–2 kun", "Pixel, CAPI va CRM ulanadi", BLUE),
               ("3-kun", "Auditoriya va tuzilma", BLUE), ("4–5 kun", "3–5 ta kreativ ishga tushadi", LIME),
               ("6–7 kun", "Tahlil: CPL va lid sifati", LIME)], footnote=M, dur=6.0),
        T_list("Shu haftada qilmaymiz", [("Har kuni", "kampaniyani o'zgartirish"),
               ("Erta", "byudjetni keskin oshirish"), ("Shoshib", "reklamani o'chirib qo'yish")],
               marker="num", dur=4.8),
        T_cta("Birinchi haftani", "biz bilan boshlang.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
