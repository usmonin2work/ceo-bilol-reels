from lib import *

CAPTION = "Lid formadagi savollar soni arizaning ham soniga, ham sifatiga bevosita ta'sir qiladi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("NECHTA SAVOL?", [("Lid formada savollar", WHITE, 92, 0), ("kam yoki ko'p", GREY, 92, 0),
               ("qaysi biri yaxshi?", LIME, 120, 1)], chart=("ARIZA", "?")),
        T_vs("Lid forma", {"title": "2 ta savol", "color": ORANGE,
               "rows": [("Ariza", "ko'p"), ("Sifat", "past bo'lishi mumkin")]},
             {"title": "4–5 ta savol", "color": TEAL,
               "rows": [("Ariza", "kamroq"), ("Sifat", "issiqroq mijozlar")]},
             ["maqsadga qarab tanlang"], footnote=M, dur=6.0),
        T_list("Qachon nima kerak", [("Kam savol", "sotuvchilar tez qo'ng'iroq qilsa"), ("Ko'p savol", "sotuv bo'limi band bo'lsa"),
               ("Saralovchi savol", "byudjet yoki muddat")], marker="check", dur=4.8),
        T_cta("Formangizni", "birga sozlaymiz.", SUB, BTN, "to'g'ri savollarni tanlab beramiz", dur=3.4),
    ]
