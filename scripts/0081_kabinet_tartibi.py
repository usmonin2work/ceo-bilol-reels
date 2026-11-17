from lib import *

CAPTION = "Reklama kabinetida aniq nomlash va tuzilma bo'lsa, qaysi reklama ishlayotganini bir qarashda ko'rasiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"

def scenes():
    return [
        T_hook("KABINET TARTIBI", [("Kabinetda", WHITE, 92, 0), ("«Yangi kampaniya 7»", GREY, 72, 0),
               ("qaysi biri ishlayapti?", LIME, 92, 1)], chart=("Nazorat", "↓")),
        T_flow("To'g'ri tuzilma", [("Kampaniya", "Maqsad", TEAL), ("Guruh", "Auditoriya", TEAL), ("Reklama", "Kreativ", LIME)],
               sub="har bir daraja — bitta vazifa", dur=6.0),
        T_list("Nomlash qoidasi", [("Maqsad", "Lid / Sotuv / Trafik"),
               ("Auditoriya", "Qiziqish / Lookalike"),
               ("Kreativ + sana", "Video1_11.17")], marker="check", dur=5.4),
        T_cta("Kabinetingizni", "birga tartiblaymiz.", SUB, BTN, "tuzilma va nomlashni tekshiramiz", dur=3.4),
    ]
