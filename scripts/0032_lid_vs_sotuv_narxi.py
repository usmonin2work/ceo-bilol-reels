from lib import *

CAPTION = "Arzon lid har doim arzon sotuv degani emas — sotuv narxiga qarang."
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("LID NARXI", [("Lid arzon,", WHITE, 110, 0), ("lekin sotuv", GREY, 90, 0),
               ("qimmat chiqyapti", LIME, 120, 1)]),
        T_list("Ikki raqam farqi", [("Lid narxi", "1 ta so'rov qancha turadi"),
               ("Sotuv narxi", "1 ta mijoz qancha turadi"), ("Konversiya", "lidlarning necha % sotiladi")],
               marker="num", footnote=M, dur=5.2),
        T_vs("Qaysi kampaniya yaxshi",
             {"title": "A kampaniya", "color": RED, "rows": [("Lid", "$1 — 100 ta"), ("Sotuv", "2 ta = $50")]},
             {"title": "B kampaniya", "color": BLUE, "rows": [("Lid", "$3 — 40 ta"), ("Sotuv", "8 ta = $15")]},
             ["Byudjetni sotuv narxi", "past kampaniyaga bering"], footnote=M, dur=6.0),
        T_cta("Lidni emas,", "sotuvni sanang.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
