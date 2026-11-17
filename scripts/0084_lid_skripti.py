from lib import *

CAPTION = "Reklama lid olib kelsa-yu sotuvchi tayyor skriptsiz gaplashsa, pullik arizalar sotuvga aylanmay qoladi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("SOTUVCHI SKRIPTI", [("Lid keldi,", WHITE, 100, 0), ("sotuvchi esa", GREY, 90, 0),
               ("nima deyishni bilmaydi", LIME, 96, 1)], chart=("Sotuvlar", "↓")),
        T_bars("100 ta lid bilan suhbat", [("Skriptsiz", 30, "3 sotuv", RED),
               ("Skript bilan", 80, "8 sotuv", LIME)],
               sub="bir xil reklama, bir xil lidlar", footnote=M, dur=5.2),
        T_list("Skriptda bo'lishi shart", [("Salomlashish", "o'zingizni va sababni ayting"),
               ("Savollar", "mijoz ehtiyojini aniqlang"),
               ("Keyingi qadam", "uchrashuv yoki to'lovga olib boring")], marker="check", dur=5.6),
        T_cta("Lid bilan ishlashni", "birga tekshiramiz.", SUB, BTN, "skriptingizdagi xatolarni ko'rsatamiz", dur=3.4),
    ]
