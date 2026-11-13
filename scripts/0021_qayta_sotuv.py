from lib import *

CAPTION = "Eski mijozlarga qayta reklama eng arzon sotuv manbai."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"

def scenes():
    return [
        T_hook("ENG ARZON SOTUV", [("Yangi mijoz qimmat,", WHITE, 100, 0), ("eski mijoz esa", GREY, 90, 0),
               ("qaytib keladi", LIME, 130, 1)]),
        T_vs("Kimga reklama?",
             {"title": "Yangi", "color": RED, "rows": [("Ishonch", "yo'q"), ("Lid narxi", "yuqori"), ("Qaror", "sekin")]},
             {"title": "Eski", "color": LIME, "rows": [("Ishonch", "bor"), ("Lid narxi", "past"), ("Qaror", "tez")]},
             ["Bazangiz —", "tayyor auditoriya"], dur=6.0),
        T_list("Qanday qilamiz", [("Baza", "mijoz raqamlarini yuklaymiz"),
               ("Taklif", "faqat ularga maxsus aksiya"), ("Takror", "har oy yangi sabab beramiz")],
               marker="check", dur=4.8),
        T_cta("Bazangizdan", "foyda olamiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
