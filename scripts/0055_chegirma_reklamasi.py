from lib import *

CAPTION = "Chegirmani doimiy emas, sababli va muddatli qiling — shunda brend arzonlashmaydi."

M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("CHEGIRMA REKLAMASI", [("Har hafta aksiya —", WHITE, 92, 0), ("mijoz to'liq narxda", GREY, 84, 0),
               ("olmay qo'yadi", LIME, 124, 1)]),
        T_vs("Bir xil 20% chegirma",
             {"title": "Doimiy aksiya", "color": ORANGE, "rows": [("Sabab", "yo'q"), ("Muddat", "cheksiz")]},
             {"title": "To'g'ri aksiya", "color": TEAL, "rows": [("Sabab", "bayram"), ("Muddat", "3 kun")]},
             ["Sabab va muddat", "qadrni saqlaydi"], footnote=M, dur=5.6),
        T_list("Brendni saqlab aksiya qilish", [("Chegirma o'rniga sovg'a", "narx tushmaydi"),
               ("Faqat obunachilarga", "yopiq taklif"), ("Aniq tugash sanasi", "shoshilish hissi")],
               marker="check", dur=4.8),
        T_cta("Aksiyani to'g'ri qiling,", "brend qadrini saqlang.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying",
              "va do'stingizga ulashing"),
    ]
