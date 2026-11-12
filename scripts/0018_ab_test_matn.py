from lib import *

CAPTION = "A/B testda bir vaqtda faqat bitta narsani o'zgartiring."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija soha va auditoriyaga bog'liq"

def scenes():
    return [
        T_hook("A/B TEST", [("Bir xil reklama,", WHITE, 100, 0), ("3 xil matn —", GREY, 90, 0),
               ("qaysi biri sotadi?", LIME, 110, 1)]),
        T_bars("Lid narxi", [("A: Narx bilan", 100, "$3.8", RED), ("B: Muammo bilan", 80, "$3.0", BLUE),
               ("C: Natija bilan", 58, "$2.2", TEAL)],
               sub="Video bir xil, faqat matn boshqa", footnote=M, dur=5.0),
        T_list("Test qoidalari", [("Bitta o'zgaruvchi", "faqat matnni almashtiring"),
               ("Teng byudjet", "har biriga bir xil summa"), ("3–5 kun", "erta xulosa qilmang")],
               marker="check", dur=4.8),
        T_cta("Testni to'g'ri", "birga quramiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
