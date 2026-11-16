from lib import *

CAPTION = "Instagram va Facebook joylashuvlarini birdaniga emas, natijaga qarab alohida tekshirib ajratish kerak."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("JOYLASHUVLAR", [("Instagram va Facebook", WHITE, 84, 0), ("bitta reklamadami?", GREY, 80, 0),
               ("raqamga qarang", LIME, 115, 1)]),
        T_bars("Bitta ariza narxi, joylashuv bo'yicha", [("Instagram Reels", 40, "40 000", LIME),
               ("Instagram Stories", 55, "55 000", TEAL), ("Facebook lenta", 70, "70 000", VIO),
               ("Audience Network", 95, "95 000", BLUE)],
               sub="har joyda narx har xil", footnote=M, dur=5.2),
        T_list("Qachon ajratish kerak", [("Boshida", "avtomatik joylashuv bilan test"),
               ("7 kundan keyin", "ariza narxini solishtiring"),
               ("Keyin", "qimmat joyni o'chiring")], marker="check", dur=5.0),
        T_cta("Reklamangizda", "qaysi joy foyda beradi?", SUB, BTN, "15 daqiqada tahlil qilib beramiz", dur=3.4),
    ]
