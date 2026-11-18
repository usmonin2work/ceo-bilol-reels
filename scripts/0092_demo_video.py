from lib import *

CAPTION = "Mahsulotni ishlatib ko'rsatgan demo video uzun tavsifdan ko'ra tezroq ishonch uyg'otadi va ariza olib keladi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("DEMO VIDEO", [("Mahsulotni maqtash", WHITE, 92, 0), ("yoki ishlatib", GREY, 90, 0),
               ("ko'rsatish?", LIME, 120, 1)], chart=("Ishonch", "↓")),
        T_vs("Bir xil mahsulot", {"title": "TAVSIF", "color": RED,
               "rows": [("Tushunarli", "qisman"), ("Ishonch", "past"), ("Arizalar", "9 ta")]},
             {"title": "DEMO", "color": LIME,
               "rows": [("Tushunarli", "darhol"), ("Ishonch", "yuqori"), ("Arizalar", "21 ta")]},
             ["Ko'rsating, tushuntirmang"], footnote=M, dur=6.2),
        T_list("Yaxshi demo", [("Muammo", "birinchi 2 soniyada"),
               ("Jarayon", "mahsulot qo'lda ishlaydi"),
               ("Natija", "oldin va keyin")], marker="check", dur=5.4),
        T_cta("Demo reklamangizni", "birga tuzamiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
