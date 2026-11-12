from lib import *

CAPTION = "Oddiy telefonda olingan video ko'pincha studiya reklamasidan yaxshiroq sotadi."
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("UGC VIDEO", [("Telefonda olingan", WHITE, 100, 0), ("oddiy video", GREY, 90, 0),
               ("ko'proq sotadi", LIME, 130, 1)]),
        T_vs("Studiya yoki UGC", {"title": "Studiya", "color": ORANGE, "rows": [("Narxi", "qimmat"), ("Ishonch", "past"),
              ("Bosish", "1%")]},
             {"title": "UGC", "color": LIME, "rows": [("Narxi", "arzon"), ("Ishonch", "yuqori"), ("Bosish", "2.5%")]},
             ["Odamlar odamga ishonadi"], footnote=M, dur=6.0),
        T_list("Yaxshi UGC qoidalari", [("Yuz bilan boshlang", "birinchi 3 soniyada"),
               ("Real tajriba", "mijoz o'z so'zi bilan"), ("Vertikal va qisqa", "15–30 soniya")],
               marker="check", dur=4.8),
        T_cta("Odamdek gapiring,", "reklamadek emas.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
