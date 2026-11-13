from lib import *

CAPTION = "Har bir ariza sifatli lid emas: ehtiyoj, byudjet va vaqtni tekshiring."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("ARIZA KO'P, SOTUV YO'Q?", [("Har bir ariza", WHITE, 100, 0), ("ham mijoz", GREY, 90, 0),
               ("emas", LIME, 130, 1)]),
        T_bars("100 ta arizadan", [("Jami arizalar", 100, "100", VIO), ("Raqami to'g'ri", 70, "70", BLUE),
               ("Javob berdi", 45, "45", TEAL), ("Sifatli lid", 20, "20", RED)],
               sub="sifatni o'lchamasangiz, pul yo'qoladi", footnote=M, dur=5.0),
        T_list("Sifatli lid belgilari", [("Ehtiyoj", "mahsulotingiz unga kerak"),
               ("Byudjet", "narxni ko'tara oladi"), ("Vaqt", "yaqin orada sotib oladi")],
               marker="check", dur=4.8),
        T_cta("Lidlaringizni", "birga baholaymiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
