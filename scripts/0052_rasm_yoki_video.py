from lib import *

CAPTION = "Rasm yoki video — qaysi biri ishlashini taxmin qilmang, bir xil byudjetda sinab ko'ring."
M = "* misol uchun, natija nishangizga bog'liq"

def scenes():
    return [
        T_hook("RASM YOKI VIDEO?", [("Qaysi biri yaxshi", WHITE, 96, 0), ("ishlashini", GREY, 90, 0),
               ("test aytadi", LIME, 130, 1)]),
        T_vs("Bir xil byudjet, 7 kun", {"title": "Rasm", "color": ORANGE, "rows": [("Byudjet", "$70"), ("Ariza", "14"),
              ("1 ariza", "$5")]},
             {"title": "Video", "color": LIME, "rows": [("Byudjet", "$70"), ("Ariza", "20"), ("1 ariza", "$3.5")]},
             ["G'olibni raqam aniqlaydi"], footnote=M, dur=6.0),
        T_list("To'g'ri test qoidalari", [("Bitta farq", "faqat format o'zgaradi"),
               ("Teng byudjet", "har biriga bir xil pul"), ("Kamida 7 kun", "keyin xulosa qiling")],
               marker="check", dur=4.8),
        T_cta("Taxmin qilmang,", "sinab ko'ring.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
