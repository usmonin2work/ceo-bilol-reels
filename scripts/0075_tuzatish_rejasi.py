from lib import *

CAPTION = "Reklamadan natija bo'lmasa, uni to'xtatishdan oldin aniq tuzatish rejasi bo'yicha qadamma-qadam tekshiramiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, muddatlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("NATIJA YO'Q", [("Reklama ishlamayapti", WHITE, 84, 0), ("to'xtatmang,", GREY, 80, 0),
               ("avval tuzating", LIME, 105, 1)]),
        T_list("Qayerdan boshlaymiz", [("Kuzatuv", "ariza to'g'ri hisoblanyaptimi"), ("Kreativ", "ilk 3 soniya ushlayaptimi"),
               ("Auditoriya", "to'g'ri odamlarga chiqyaptimi"), ("Taklif", "nega aynan sizdan olish kerak")], dur=5.2),
        T_flow("Tuzatish rejasi", [("1-3 kun", "Kuzatuv va tahlil", VIO), ("4-7 kun", "Yangi kreativlar", BLUE),
               ("8-14 kun", "Auditoriya testi", TEAL), ("Natija", "Eng yaxshisini kuchaytirish", LIME)],
               footnote=M, dur=6.0),
        T_cta("Reklamangiz natija", "bermayaptimi?", SUB, BTN, "15 daqiqada sababini topamiz", dur=3.4),
    ]
