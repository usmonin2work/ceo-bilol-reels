from lib import *

CAPTION = "Mamnun mijozning bitta sharhi yaxshi tayyorlansa, eng ishonchli video reklamaga aylanadi."

def scenes():
    return [
        T_hook("SHARHDAN REKLAMA", [("Eng yaxshi reklama", WHITE, 92, 0), ("matni allaqachon", GREY, 88, 0),
               ("mijozda bor", LIME, 128, 1)]),
        T_flow("Sharhni videoga aylantirish", [("1-qadam", "Sharhni tanlang", TEAL),
               ("2-qadam", "Muammo → natija", ORANGE), ("3-qadam", "Qisqa video, 15 s", WHITE),
               ("Natija", "Ishonchli reklama", LIME)], dur=5.6),
        T_list("Video ichida bo'lsin", [("Real yuz yoki ovoz", "aktyor emas, mijoz"),
               ("Aniq natija", "nima o'zgardi"), ("Subtitr", "ovozsiz ham tushunarli")],
               marker="check", dur=4.8),
        T_cta("Sharhlarni yig'ing,", "reklamaga aylantiring.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying",
              "va do'stingizga ulashing"),
    ]
