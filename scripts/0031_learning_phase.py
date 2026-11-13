from lib import *

CAPTION = "Reklamani har kuni o'zgartirsangiz, algoritm o'rganishni qaytadan boshlaydi."
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("LEARNING PHASE", [("Har kuni", WHITE, 110, 0), ("o'zgartirsangiz,", GREY, 90, 0),
               ("natija kelmaydi", LIME, 120, 1)]),
        T_list("O'rganish davri nima?", [("Maqsad", "~50 ta natija yig'ish"),
               ("Muddat", "odatda 5–7 kun"), ("Bu vaqtda", "narx o'zgaruvchan bo'ladi")],
               marker="num", footnote=M, dur=5.2),
        T_vs("O'rganishni nima buzadi",
             {"title": "Qayta boshlanadi", "color": RED, "rows": [("Byudjet", "keskin o'zgarsa"), ("Auditoriya", "tahrirlansa")]},
             {"title": "Xavfsiz", "color": BLUE, "rows": [("Yangi kreativ", "alohida ad setda"), ("Byudjet", "20% gacha qadam")]},
             ["Sabr qiling,", "raqamlarni haftada baholang"], dur=6.0),
        T_cta("O'rganishga", "vaqt bering.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
