from lib import *

CAPTION = "Yangi biznesda reklamani yoqishdan oldin taklif, narx va javob berish tizimi tayyor bo'lishi kerak."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("YANGI BIZNES", [("Reklamani yoqishga", WHITE, 96, 0), ("shoshilmang —", GREY, 90, 0),
               ("avval tekshiring", LIME, 124, 1)], chart=("BYUDJET", "↓")),
        T_list("Biz tekshiradigan ro'yxat", [("Taklif", "nega aynan sizdan olish kerak"), ("Narx", "aniq yoki «dan boshlab»"),
               ("Javob", "arizaga 15 daqiqada qo'ng'iroq"), ("Test byudjeti", "kamida 2 hafta uchun")],
               marker="check", dur=5.6),
        T_vs("Bir xil byudjet", {"title": "Tayyor emas", "color": RED,
               "rows": [("Ariza", "keladi"), ("Sotuv", "deyarli yo'q")]},
             {"title": "Tayyor", "color": TEAL,
               "rows": [("Ariza", "keladi"), ("Sotuv", "barqaror")]},
             ["farq — reklamagacha bo'lgan ishda"], footnote=M, dur=6.0),
        T_cta("Biznesingizni", "reklamaga tayyorlaymiz.", SUB, BTN, "ro'yxat bo'yicha birga tekshiramiz", dur=3.4),
    ]
