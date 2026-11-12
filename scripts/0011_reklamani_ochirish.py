from lib import *

CAPTION = "Reklamani qachon o'chirish kerakligini 3 ta aniq signal ko'rsatadi."
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("QACHON O'CHIRISH KERAK?", [("Reklamani", WHITE, 110, 0), ("o'chirish", GREY, 90, 0),
               ("vaqti keldimi?", LIME, 130, 1)], chart=("Natija", "↓")),
        T_list("3 ta aniq signal", [("Lid narxi", "2 baravar oshdi"),
               ("Chastota", "3 dan yuqori, CTR tushdi"), ("Sotuv", "7 kunda bitta ham yo'q")],
               marker="num", footnote=M, dur=5.2),
        T_vs("O'chirishdan oldin",
             {"title": "Shoshilmang", "color": BLUE, "rows": [("1–2 kun", "kam ma'lumot"), ("Yangi kreativ", "o'rganish davri")]},
             {"title": "O'chiring", "color": RED, "rows": [("Signal", "3 kun takrorlansa"), ("Byudjet", "foydasiz ketsa")]},
             ["Hissiyot emas,", "raqamga qarab qaror qiling"], dur=6.0),
        T_cta("Raqamga qarab", "qaror qiling.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
