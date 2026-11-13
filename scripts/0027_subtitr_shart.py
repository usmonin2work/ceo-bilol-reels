from lib import *

CAPTION = "Video reklamaga subtitr qo'shing: ko'pchilik uni ovozsiz ko'radi."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, raqamlar biznesingizga bog'liq"

def scenes():
    return [
        T_hook("VIDEONGIZ OVOZSIZ KO'RILYAPTI", [("Gapiryapsiz,", WHITE, 100, 0), ("lekin hech kim", GREY, 90, 0),
               ("eshitmayapti", LIME, 120, 1)]),
        T_bars("Video oxirigacha ko'rildi", [("Subtitrsiz", 35, "18%", RED), ("Subtitr bilan", 100, "41%", TEAL)],
               sub="odamlar ko'pincha ovozsiz aylantiradi", footnote=M, dur=5.0),
        T_list("To'g'ri subtitr", [("Katta", "telefonda oson o'qilsin"),
               ("Qisqa", "bir qatorda 3-5 so'z"), ("Markazda", "tugmalar ostida qolmasin")],
               marker="check", dur=4.8),
        T_cta("Videolaringizni", "birga tekshiramiz.", SUB, BTN, "15 daqiqalik bepul audit", dur=3.4),
    ]
