from lib import *

CAPTION = "Look-alike auditoriya manbasiga qarab ishlaydi — eng yaxshisini tanlang."
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("LOOK-ALIKE", [("O'xshash auditoriya", WHITE, 100, 0), ("manbasi", GREY, 90, 0),
               ("hamma narsani hal qiladi", LIME, 110, 1)]),
        T_bars("Manba sifati", [("Xaridorlar ro'yxati", 100, "eng yaxshi", LIME), ("Sifatli lidlar", 75, "yaxshi", TEAL),
               ("Sayt mehmonlari", 45, "o'rtacha", ORANGE), ("Layk bosganlar", 20, "past", RED)],
               sub="qanchalik sotuvga yaqin", footnote=M, dur=5.0),
        T_list("Qoidalar", [("Kamida 100 ta xaridor", "kam bo'lsa — sifatli lidlar"),
               ("1% dan boshlang", "keyin 3–5% gacha kengaytiring"), ("Ro'yxatni yangilang", "har oy yangi xaridorlar")],
               marker="check", dur=4.8),
        T_cta("Manba to'g'ri bo'lsa,", "auditoriya ishlaydi.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
