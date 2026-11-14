from lib import *

CAPTION = "Eng yaxshi kreativ ham charchaydi — yangilarini har 2–3 haftada qo'shib boring."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, ritm byudjet va auditoriya hajmiga bog'liq"

def scenes():
    return [
        T_hook("KREATIV RITMI", [("Video zo'r ishladi.", WHITE, 90, 0), ("Endi lid qimmat.", GREY, 100, 0),
               ("Kreativ charchadi", LIME, 120, 1)]),
        T_bars("Bitta kreativda lid narxi", [("1-hafta", 1.0, "$1.0", LIME), ("2-hafta", 1.3, "$1.3", BLUE),
               ("3-hafta", 1.9, "$1.9", GREY), ("4-hafta", 2.8, "$2.8", RED)], footnote=M, dur=5.2),
        T_list("Yangilash ritmi", [("Har 2–3 hafta", "1–2 ta yangi video"),
               ("Chastota 3 dan oshsa", "darhol almashtiring"),
               ("G'olibni saqlang", "yangi variant bilan sinang")], marker="check", dur=5.0),
        T_cta("Kreativlaringizni", "tahlil qilamiz.", SUB, BTN, "15 daqiqada kabinetni ko'rib chiqamiz", dur=3.4),
    ]
