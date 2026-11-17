from lib import *

CAPTION = "Mijoz bir marta emas, qayta-qayta xarid qilsa, reklamaga qancha sarflash mumkinligini LTV ko'rsatadi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("LTV NIMA?", [("Mijoz bir marta", WHITE, 96, 0), ("emas, qayta-qayta", GREY, 84, 0),
               ("xarid qiladi", LIME, 120, 1)], chart=("Bir martalik hisob", "↓")),
        T_formula("Mijoz qiymati (LTV)", "Chek × Xaridlar soni", [("O'rtacha chek", TEAL, "200 000 so'm"),
               ("Yiliga xarid", BLUE, "5 marta"), ("LTV", LIME, "1 000 000 so'm")],
               footnote=M, dur=5.4),
        T_vs("Mijozga qancha to'lash mumkin?",
             {"title": "1-xarid", "color": RED, "rows": [("Daromad", "200 000"), ("Lid chegarasi", "50 000")]},
             {"title": "LTV", "color": LIME, "rows": [("Daromad", "1 000 000"), ("Lid chegarasi", "200 000")]},
             ["LTV bilan reklamani dadil kengaytirasiz"], footnote=M, dur=6.0),
        T_cta("Mijoz qiymatini", "birga hisoblaymiz.", SUB, BTN, "mijoz narxi chegarasini topamiz", dur=3.4),
    ]
