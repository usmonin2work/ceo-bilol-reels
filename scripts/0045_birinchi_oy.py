from lib import *

CAPTION = "Kichik biznes reklamaning birinchi oyida sotuvdan oldin to'g'ri ma'lumot yig'ishi kerak."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, muddat soha va byudjetga bog'liq"

def scenes():
    return [
        T_hook("BIRINCHI OY", [("Reklamani endi", WHITE, 100, 0), ("boshlayapsizmi?", GREY, 100, 0),
               ("Shoshilmang", LIME, 130, 1)]),
        T_flow("Birinchi oy rejasi", [("1-hafta", "3 xil taklif sinovi", WHITE),
               ("2-hafta", "Yutgan kreativlar", BLUE), ("3-hafta", "Auditoriyani toraytirish", TEAL),
               ("4-hafta", "Byudjetni oshirish", LIME)], footnote=M, dur=6.0, step=0.7),
        T_list("Birinchi oyda qilmang", [("Katta byudjet", "sinovsiz pul ketadi"),
               ("Har kuni o'zgartirish", "algoritm o'rganolmaydi"),
               ("Faqat layklarga qarash", "arizalarni sanang")], marker="num", dur=5.0),
        T_cta("Birinchi oyni", "birga rejalaymiz.", SUB, BTN, "15 daqiqada kabinetni ko'rib chiqamiz", dur=3.4),
    ]
