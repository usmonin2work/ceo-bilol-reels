from lib import *

CAPTION = "Yosh va jins bo'yicha auditoriyani tor cheklash faqat mahsulot aniq bir guruhga mo'ljallangan bo'lsa foydali."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("YOSH VA JINS", [("Auditoriyani", WHITE, 92, 0), ("tor cheklash", GREY, 90, 0),
               ("har doim kerakmi?", LIME, 110, 1)], chart=("Qamrov", "↓")),
        T_vs("Kosmetika do'koni uchun", {"title": "Tor", "color": RED,
               "rows": [("Auditoriya", "ayollar 25–30"), ("Qamrov", "kichik"), ("Lid narxi", "~25 000")]},
             {"title": "Keng", "color": TEAL,
               "rows": [("Auditoriya", "ayollar 18–45"), ("Qamrov", "katta"), ("Lid narxi", "~14 000")]},
             ["algoritmga joy bering"], footnote=M, dur=6.0),
        T_list("Qachon cheklash kerak", [("Mahsulot", "faqat bir jinsga bo'lsa"),
               ("Qonun", "18+ talab qilinsa"),
               ("Qolgan holat", "keng qoldiring, kreativ tanlaydi")], marker="num", dur=5.4),
        T_cta("Auditoriya sozlamangizni", "tekshirib beramiz.", SUB, BTN, "ortiqcha cheklovlarni ko'rasiz", dur=3.4),
    ]
