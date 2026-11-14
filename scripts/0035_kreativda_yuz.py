from lib import *

CAPTION = "Kreativda inson yuzini ko'rsatish reklamangizni ko'proq to'xtatib ko'radigan qilishi mumkin."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("YUZ KO'RINADIMI?", [("Odamlar lentada", WHITE, 100, 0), ("mahsulotdan oldin", GREY, 90, 0),
               ("yuzga qaraydi", LIME, 130, 1)], chart=("Yuzsiz kreativ CTR", "↓")),
        T_bars("Kreativ turi va CTR", [("Yuz + matn", 100, "1.8%", TEAL), ("Faqat mahsulot", 60, "1.1%", BLUE),
               ("Faqat matn", 35, "0.6%", RED)], sub="bir xil auditoriyada test", footnote=M, dur=5.0),
        T_list("Yuzni to'g'ri ko'rsating", [("Ko'z kameraga", "birinchi soniyada qarash"), ("Haqiqiy odam", "stok rasm emas"),
               ("A/B test", "yuzli va yuzsiz variant")], marker="check", dur=5.0),
        T_cta("Yuz ko'rinsa,", "ishonch ortadi.", SUB, BTN, "15 daqiqada kreativingizni tahlil qilamiz", dur=3.4),
    ]
