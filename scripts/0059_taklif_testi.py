from lib import *

CAPTION = "Qaysi taklif ko'proq ariza berishini taxmin qilmang — bir nechtasini bir vaqtda sinab ko'ring."

M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("TAKLIF TESTI", [("Reklama bir,", WHITE, 100, 0), ("taklif esa", GREY, 90, 0),
               ("har xil", LIME, 130, 1)], chart=("Arizalar", "↓")),
        T_bars("Bir xil byudjetda 1 hafta — arizalar", [("Chegirma 10%", 18, "18", BLUE),
               ("Bepul yetkazish", 31, "31", TEAL), ("Sovg'a bilan", 24, "24", ORANGE), ("Bepul konsultatsiya", 42, "42", LIME)],
               sub="g'olib taklifga byudjetni o'tkazing", footnote=M, dur=5.0),
        T_list("Taklifni to'g'ri sinash", [("Bitta farq", "faqat taklifni o'zgartiring"), ("Teng byudjet", "har biriga bir xil pul"),
               ("Yetarli vaqt", "kamida 3–7 kun kuting")], marker="check", dur=4.8),
        T_cta("Sinab ko'ring —", "keyin kuchaytiring.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying",
              "va do'stingizga ulashing"),
    ]
