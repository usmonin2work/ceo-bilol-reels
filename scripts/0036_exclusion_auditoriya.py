from lib import *

CAPTION = "Mavjud mijozlarni reklamadan chiqarib tashlasangiz, byudjet yangi odamlarga sarflanadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("PULINGIZ KIMGA KETYAPTI?", [("Reklamangizni", WHITE, 100, 0), ("eski mijozlar", GREY, 90, 0),
               ("qayta ko'ryapti", LIME, 130, 1)], chart=("Yangi mijozlar", "↓")),
        T_vs("Exclusion bilan farq", {"title": "Exclusionsiz", "color": RED, "rows": [("Eski mijozlarga", "30%"), ("Yangi lid narxi", "$4.0")]},
             {"title": "Exclusion bilan", "color": TEAL, "rows": [("Eski mijozlarga", "0%"), ("Yangi lid narxi", "$2.9")]},
             ["Byudjet yangi odamlarga ketadi"], footnote=M, dur=6.0),
        T_list("Kimni chiqarish kerak", [("Xaridorlar", "CRM ro'yxatini yuklang"), ("Ariza qoldirganlar", "oxirgi 30 kun"),
               ("Xodimlar", "va sahifa adminlari")], marker="check", dur=5.0),
        T_cta("Auditoriyangizni", "birga tozalaymiz.", SUB, BTN, "15 daqiqada kabinetingizni tekshiramiz", dur=3.4),
    ]
