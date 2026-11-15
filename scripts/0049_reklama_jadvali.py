from lib import *

CAPTION = "Mijozlaringiz qaysi soatlarda yozishini bilsangiz, reklamani aynan o'sha vaqtga jamlash mumkin."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, har bir biznesda soatlar har xil"

def scenes():
    return [
        T_hook("REKLAMA KECHASI HAM ISHLAYAPTIMI?", [("Siz uxlayapsiz,", WHITE, 100, 0), ("reklama esa", GREY, 90, 0),
               ("pul sarflayapti", LIME, 130, 1)], chart=("Byudjet", "↓")),
        T_bars("Arizalar qachon keladi", [("09:00–13:00", 100, "35%", VIO), ("13:00–18:00", 71, "25%", BLUE),
               ("18:00–23:00", 97, "34%", TEAL), ("23:00–09:00", 17, "6%", RED)],
               sub="kechasi pul ketadi, ariza kelmaydi", footnote=M, dur=5.0),
        T_list("Jadvalni 3 qadamda quramiz", [("Ma'lumot", "2 haftalik arizalar soati"),
               ("Jadval", "faol soat va kunlarni tanlash"),
               ("Javob", "menejer shu soatlarda onlayn")], marker="check", dur=4.8),
        T_cta("Reklamangizni", "soatga sozlaymiz.", SUB, BTN, "15 daqiqada jadvalni ko'rsatamiz", dur=3.4),
    ]
