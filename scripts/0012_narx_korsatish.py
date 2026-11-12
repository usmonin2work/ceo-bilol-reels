from lib import *

CAPTION = "Narxni reklamada ko'rsatish lidlarni kamaytiradi, lekin sifatini oshiradi."
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("NARXNI YOZISH KERAKMI?", [("Reklamada", WHITE, 110, 0), ("narxni", GREY, 90, 0),
               ("ko'rsatasizmi?", LIME, 130, 1)]),
        T_vs("Ikki yo'l",
             {"title": "Narxsiz", "color": BLUE, "rows": [("Lid", "ko'p va arzon"), ("Sifat", "ko'pi «shunchaki»")]},
             {"title": "Narx bilan", "color": LIME, "rows": [("Lid", "kamroq"), ("Sifat", "tayyor xaridor")]},
             ["Sotuv bo'limi kichik bo'lsa,", "narxni ko'rsatish foydali"], footnote=M, dur=6.0),
        T_list("Qachon ko'rsatish kerak", [("Narx raqobatbardosh", "bozordan arzon yoki teng"),
               ("Mahsulot oddiy", "tushuntirish shart emas"), ("Vaqt tejash", "menejer «narx?»ga javob bermaydi")],
               marker="check", dur=5.0),
        T_cta("Ikkalasini ham", "test qilib ko'ring.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
