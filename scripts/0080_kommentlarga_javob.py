from lib import *

CAPTION = "Reklama ostidagi izohlarga tez va aniq javob berish ishonchni oshiradi va arizaga aylanadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("IZOHLAR SOTADI", [("Reklama ostida", WHITE, 92, 0), ("«narxi qancha?» deb", GREY, 76, 0),
               ("javobsiz qoldimi?", LIME, 104, 1)], chart=("Ariza", "↓")),
        T_vs("Bir xil reklama, izohlarda", {"title": "Javobsiz", "color": RED,
               "rows": [("Javob", "1 kundan keyin"), ("Ishonch", "past"), ("Ariza", "~3 ta")]},
             {"title": "Tez javob", "color": TEAL,
               "rows": [("Javob", "1 soat ichida"), ("Ishonch", "yuqori"), ("Ariza", "~8 ta")]},
             ["izoh — ochiq turgan savdo"], footnote=M, dur=6.0),
        T_list("Javob qoidasi", [("Tez", "1 soat ichida javob"),
               ("Aniq", "savolga to'g'ridan-to'g'ri"),
               ("Keyingi qadam", "Direct'ga taklif qiling")], marker="check", dur=5.4),
        T_cta("Reklamangizni", "birga ko'rib chiqamiz.", SUB, BTN, "izohlarni arizaga aylantiramiz", dur=3.4),
    ]
