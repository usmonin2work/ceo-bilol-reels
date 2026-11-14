from lib import *

CAPTION = "Xabarlar kampaniyasi suhbat orqali sotiladigan mahsulotlar uchun eng qulay yo'l."
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("DIRECT REKLAMASI", [("Mijoz sayt emas,", WHITE, 100, 0), ("Direct'ga", GREY, 90, 0),
               ("yozishni xohlaydi", LIME, 120, 1)]),
        T_list("Qachon foydali", [("Narx savol tug'diradi", "maslahat kerak bo'lgan xizmat"),
               ("Sayt yo'q", "Instagram — asosiy do'kon"), ("Tez javob bera olasiz", "5 daqiqada, ish vaqtida")],
               marker="check", dur=5.0),
        T_vs("Qaysi biri qachon",
             {"title": "Xabarlar", "color": BLUE, "rows": [("Mos", "xizmat, kurs"), ("Shart", "tez javob")]},
             {"title": "Lid forma", "color": VIO, "rows": [("Mos", "ko'p ariza"), ("Shart", "qo'ng'iroq")]},
             ["Javob kechiksa,", "Direct lidi sovib qoladi"], footnote=M, dur=6.0),
        T_cta("Suhbatdan", "sotuvgacha.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
