# Example script. Copy it to scripts/NNNN_short_name.py and change the texts.
# Colours: WHITE, LIME, VIO, BLUE, TEAL, RED, GREY, ORANGE. Keep every line short (it must fit 1080 px).
from lib import *

CAPTION = "Reklama ishlayapti, lekin mijoz yo'lda yo'qolyaptimi?"

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        # 1) hook: tag line (typed), 2-4 lines; last tuple flag 1 = pop-in accent line. chart= adds falling red line.
        T_hook("MIJOZ QAYERDA YO'QOLYAPTI?", [("Reklama ishlayapti,", WHITE, 100, 0), ("mijoz esa", GREY, 90, 0),
               ("yo'lda yo'qolyapti", LIME, 130, 1)], chart=("Sotuvlar", "↓")),
        # 2) body scenes: pick 2 of T_bars / T_list / T_vs / T_flow / T_cards / T_formula / T_big / T_title
        T_bars("100 ta arizadan", [("Ariza qoldirdi", 100, "100", VIO), ("Vaqtida javob oldi", 60, "60", BLUE),
               ("Suhbat bo'ldi", 35, "35", TEAL), ("Sotib oldi", 8, "8", RED)],
               sub="har bosqichda odam yo'qoladi", footnote=M, dur=5.0),
        T_list("Biz 3 joyni tuzatamiz", [("Reklama", "to'g'ri odamga, to'g'ri taklif"), ("Sahifa", "klik arizaga aylansin"),
               ("Sotuv bilan aloqa", "lid sovib qolmasin")], marker="check", dur=4.6),
        # 3) CTA
        T_cta("Voronkangizni", "birga tekshiramiz.", SUB, BTN, "15 daqiqada teshiklarni ko'rsatamiz", dur=3.4),
    ]
