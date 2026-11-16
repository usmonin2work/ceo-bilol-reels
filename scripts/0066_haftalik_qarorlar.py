from lib import *

CAPTION = "Reklamani his bilan emas, har hafta aniq raqamlarga qarab qaror qabul qilib boshqaramiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("HAFTALIK RITM", [("Reklama his bilan", WHITE, 96, 0), ("emas,", GREY, 90, 0),
               ("raqam bilan", LIME, 130, 1)], chart=("Isrof", "↓")),
        T_flow("Har dushanba", [("1-qadam", "O'tgan hafta raqamlari", WHITE),
               ("2-qadam", "Ariza va sotuv narxi", BLUE), ("3-qadam", "Kuchsizini o'chiramiz", TEAL),
               ("4-qadam", "Yutganiga byudjet", LIME)], footnote=M, dur=6.0, step=0.7),
        T_list("3 ta qoida", [("Ariza qimmat", "kreativni almashtiramiz"),
               ("Sotuv yo'q", "taklif va javobni tekshiramiz"),
               ("Hammasi yaxshi", "byudjetni 20% oshiramiz")], marker="num", footnote=M, dur=5.4),
        T_cta("Reklamangizga", "ritm beramiz.", SUB, BTN, "har hafta aniq qaror va hisobot", dur=3.4),
    ]
