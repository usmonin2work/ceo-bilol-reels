from lib import *

CAPTION = "Kafolat va risksiz taklif mijozning qo'rquvini kamaytiradi va ariza qoldirishni osonlashtiradi."
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("RISKSIZ TAKLIF", [("Mijoz sotib olmaydi,", WHITE, 92, 0), ("chunki qo'rqadi", GREY, 88, 0),
               ("kafolat yordam beradi", LIME, 104, 1)]),
        T_vs("Bir xil reklama", {"title": "Kafolatsiz", "color": ORANGE, "rows": [("Ishonch", "past"), ("Savollar", "ko'p"),
              ("Ariza", "1%")]},
             {"title": "Kafolat bilan", "color": LIME, "rows": [("Ishonch", "yuqori"), ("Savollar", "kam"), ("Ariza", "2%")]},
             ["Risk sizda — qaror mijozda oson"], footnote=M, dur=6.0),
        T_list("Kafolat turlari", [("Pulni qaytarish", "yoqmasa — 7 kun ichida"),
               ("Bepul sinov", "avval ko'rib, keyin to'lov"), ("Natija kafolati", "aniq va o'lchanadigan")],
               marker="check", dur=4.8),
        T_cta("Kafolat bering,", "ishonch oshadi.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
