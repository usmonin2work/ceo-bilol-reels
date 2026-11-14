from lib import *

CAPTION = "Raqobatchilaringiz qaysi reklamalarni aylantirayotganini Ad Library orqali tahlil qilib beramiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"

def scenes():
    return [
        T_hook("RAQOBATCHINGIZ NIMA QILYAPTI?", [("Uning reklamalari", WHITE, 100, 0), ("hammaga ochiq", GREY, 90, 0),
               ("Ad Library'da", LIME, 130, 1)]),
        T_flow("Qanday tahlil qilamiz", [("1-qadam", "Raqobatchilarni topamiz", VIO),
               ("2-qadam", "Faol reklamalarni yig'amiz", BLUE), ("3-qadam", "Uzoq turganlarini ajratamiz", TEAL),
               ("Natija", "Sizga mos g'oyalar", LIME)], dur=6.0),
        T_list("Nimaga qaraymiz", [("Oferta", "qanday taklif qilyapti"), ("Format", "video, rasm yoki karusel"),
               ("Muddat", "uzoq yurgan reklama ishlaydi")], marker="check", dur=5.0),
        T_cta("Raqobatchilaringizni", "birga tahlil qilamiz.", SUB, BTN, "15 daqiqada asosiy xulosalar", dur=3.4),
    ]
