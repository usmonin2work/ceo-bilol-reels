from lib import *

CAPTION = "CBO va ABO: byudjetni kampaniya yoki ad set darajasida taqsimlash farqi."
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("BYUDJET QAYERDA TURADI?", [("CBO", WHITE, 130, 0), ("yoki", GREY, 90, 0),
               ("ABO?", LIME, 130, 1)]),
        T_vs("Ikki yo'l",
             {"title": "ABO", "color": BLUE, "rows": [("Byudjet", "har ad set alohida"), ("Nazorat", "to'liq qo'lda")]},
             {"title": "CBO", "color": LIME, "rows": [("Byudjet", "kampaniya darajasida"), ("Nazorat", "algoritm taqsimlaydi")]},
             ["Masalan, 3 ta ad set,", "kuniga $30 jami"], footnote=M, dur=6.0),
        T_list("Qachon nima", [("Test bosqichi", "ABO — har biriga teng imkon"),
               ("G'olib topildi", "CBO — pulni o'zi yo'naltiradi"), ("Masshtab", "CBO + kuchli kreativlar")],
               marker="check", dur=5.0),
        T_cta("Avval ABO — test,", "keyin CBO — o'sish.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
