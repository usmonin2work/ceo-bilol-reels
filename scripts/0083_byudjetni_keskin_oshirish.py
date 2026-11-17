from lib import *

CAPTION = "Ishlayotgan reklamaning kunlik byudjetini birdan ikki barobar oshirsangiz, natija yaxshilanish o'rniga tushib ketishi mumkin."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("BYUDJET XATOSI", [("Reklama ishladi —", WHITE, 92, 0), ("byudjetni 2 barobar", GREY, 80, 0),
               ("oshirdingiz?", LIME, 120, 1)], chart=("Lid narxi", "↑")),
        T_bars("Keskin oshirgandan keyin", [("Oldin: 100 000 so'm/kun", 20, "20 000", LIME),
               ("Keyin: 200 000 so'm/kun", 45, "45 000", RED)],
               sub="bitta lid narxi, so'm", footnote=M, dur=5.4),
        T_list("To'g'ri yo'l", [("Asta-sekin", "har 2–3 kunda +20–30%"),
               ("O'qish bosqichi", "algoritmni qayta boshlatmang"),
               ("Natijani kuzating", "lid narxi barqaror bo'lsa — davom")], marker="check", dur=5.6),
        T_cta("Byudjetni xavfsiz", "birga oshiramiz.", SUB, BTN, "kengaytirish rejasini tuzamiz", dur=3.4),
    ]
