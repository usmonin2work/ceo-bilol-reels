from lib import *

CAPTION = "Byudjetingizning qaysi qismi sotuv keltirib, qaysi qismi bekorga ketayotganini auditda ko'rsatamiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, har bir kabinet har xil"

def scenes():
    return [
        T_hook("PULINGIZ QAYERGA KETYAPTI?", [("Oyiga $1000 reklama,", WHITE, 92, 0), ("lekin qaysi biri", GREY, 86, 0),
               ("sotyapti?", LIME, 130, 1)], chart=("Aniqlik", "↓")),
        T_bars("Odatdagi kabinetda $1000", [("Sotuv keltiradi", 35, "$350", LIME), ("Faqat lid yig'adi", 25, "$250", TEAL),
               ("Charchagan kreativ", 22, "$220", ORANGE), ("Natijasiz", 18, "$180", RED)],
               sub="byudjet taqsimoti", footnote=M, dur=5.2),
        T_list("Auditda 3 narsani ko'rsatamiz", [("Ishlayotgan", "pulni ko'paytirish kerak bo'lgan joy"),
               ("Kuyayotgan", "darhol o'chiriladigan reklamalar"),
               ("Yangi", "sinab ko'rish kerak bo'lgan yo'nalish")], marker="check", dur=5.0),
        T_cta("Byudjetingiz xaritasini", "chizib beramiz.", SUB, BTN, "15 daqiqada ko'rsatamiz", dur=3.4),
    ]
