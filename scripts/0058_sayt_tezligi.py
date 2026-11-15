from lib import *

CAPTION = "Sahifangiz sekin ochilsa, reklamaga to'lagan klikingiz ariza bo'lmasdan yo'qoladi."

M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("SAYT TEZLIGI", [("Klik bor,", WHITE, 100, 0), ("ariza esa", GREY, 90, 0),
               ("kam keladi", LIME, 130, 1)], chart=("Arizalar", "↓")),
        T_bars("100 ta klikdan sahifani kutganlar", [("1 soniyada", 90, "90", TEAL),
               ("3 soniyada", 65, "65", BLUE), ("6 soniyada", 40, "40", ORANGE), ("10 soniyada", 20, "20", RED)],
               sub="har soniya — yo'qolgan mijoz", footnote=M, dur=5.0),
        T_list("Sahifani tezlashtirish", [("Rasmlar", "hajmini kichraytiring"), ("Ortiqcha kod", "keraksiz vidjetlarni olib tashlang"),
               ("Telefonda tekshiring", "mijozlar u yerdan kiradi")], marker="check", dur=4.8),
        T_cta("Tez sahifa —", "arzon ariza.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying",
              "va do'stingizga ulashing"),
    ]
