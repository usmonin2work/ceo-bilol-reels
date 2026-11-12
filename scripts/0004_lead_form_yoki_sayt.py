from lib import *

CAPTION = "Lead form tez lid beradi, sayt esa sifatliroq — qaysi biri sizga mos?"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("LEAD FORM YOKI SAYT?", [("Arzon lidmi", WHITE, 110, 0), ("yoki", GREY, 90, 0),
               ("sifatli lid?", LIME, 140, 1)]),
        T_vs("Bir xil byudjet",
             {"title": "Lead form", "color": BLUE, "rows": [("Lid narxi", "arzon"), ("Lidlar", "ko'p"), ("Sifati", "past")]},
             {"title": "Sayt", "color": LIME, "rows": [("Lid narxi", "qimmatroq"), ("Lidlar", "kamroq"), ("Sifati", "yuqori")]},
             ["Ko'p lid emas,", "sotuvga aylangan lid muhim"], dur=6.0),
        T_list("Qachon nimani tanlash", [("Lead form", "oddiy, arzon mahsulot va tez qo'ng'iroq"),
               ("Sayt", "qimmat yoki murakkab xizmat"), ("Ikkalasi", "formaga savol qo'shib, filtrlang")],
               marker="check", dur=4.8),
        T_cta("Lid emas,", "sotuvni hisoblang.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
