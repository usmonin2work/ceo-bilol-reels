from lib import *

CAPTION = "Reklama birdan qimmatlashdimi? Ehtimol, kreativ charchagan."
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("KREATIV CHARCHASHI", [("Reklama yaxshi", WHITE, 110, 0), ("ishlardi,", WHITE, 100, 0),
               ("endi qimmat", LIME, 140, 1)], chart=("Natija", "↓")),
        T_bars("Frequency oshgan sari", [("1–2 marta", 100, "100%", LIME), ("3 marta", 75, "75%", TEAL),
               ("4 marta", 50, "50%", ORANGE), ("5+ marta", 30, "30%", RED)],
               sub="reklamaga bosish ulushi", footnote=M, dur=5.0),
        T_list("Nima qilish kerak", [("Frequency'ni kuzating", "3 dan oshsa — signal"),
               ("Yangi hook qo'ying", "boshlanishni almashtiring"), ("Har hafta yangi kreativ", "zaxirada 3–5 ta tursin")],
               marker="check", dur=4.8),
        T_cta("Kreativni", "vaqtida yangilang.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
