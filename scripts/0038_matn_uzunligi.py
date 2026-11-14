from lib import *

CAPTION = "Qisqa yoki uzun reklama matni — qaysi biri yutishi mahsulotingizga bog'liq."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"

def scenes():
    return [
        T_hook("QISQA YOKI UZUN?", [("Reklama matni", WHITE, 100, 0), ("qancha uzun", GREY, 90, 0),
               ("bo'lishi kerak?", LIME, 130, 1)]),
        T_vs("Qachon qaysi biri?", {"title": "QISQA", "color": LIME,
               "rows": [("Narx", "arzon"), ("Qaror", "tez"), ("Mahsulot", "tanish")]},
             {"title": "UZUN", "color": BLUE,
               "rows": [("Narx", "qimmat"), ("Qaror", "o'ylab"), ("Mahsulot", "yangi")]},
             ["Matn savollarga javob bersin"], dur=6.0),
        T_list("Har qanday matnda", [("1-qator", "eng kuchli fikr"), ("Aniq taklif", "nima va kimga"),
               ("Bitta CTA", "keyingi qadam aniq")], marker="check", dur=5.0),
        T_cta("Ikkalasini", "test qiling.", SUB, BTN, "15 daqiqada matningizni tahlil qilamiz", dur=3.4),
    ]
