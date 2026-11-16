from lib import *

CAPTION = "Arizalarni Excel'da yig'sangiz, qaysi reklama sotuv olib kelganini hech qachon aniq bilmaysiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, natija biznesingizga bog'liq"

def scenes():
    return [
        T_hook("ARIZALAR EXCEL'DAMI?", [("Ariza keldi,", WHITE, 100, 0), ("sotuv bo'ldimi —", GREY, 90, 0),
               ("hech kim bilmaydi", LIME, 124, 1)], chart=("Nazorat", "↓")),
        T_vs("Bir xil 100 ta ariza", {"title": "Excel", "color": RED,
               "rows": [("Manba", "unutiladi"), ("Holat", "eskiradi"), ("Sotuv", "ko'rinmaydi")]},
             {"title": "CRM", "color": TEAL,
               "rows": [("Manba", "avtomatik"), ("Holat", "har kuni"), ("Sotuv", "reklamaga bog'liq")]},
             ["byudjet sotuvga qarab taqsimlanadi"], footnote=M, dur=6.0),
        T_flow("CRM'da bitta lid yo'li", [("Reklama", "Qaysi kreativdan", VIO), ("Ariza", "Avtomatik tushadi", BLUE),
               ("Menejer", "Holatni belgilaydi", TEAL), ("Natija", "Sotuv summasi", LIME)], dur=5.6),
        T_cta("Reklama va CRM'ni", "birga ulaymiz.", SUB, BTN, "qaysi kampaniya pul topayotganini ko'rasiz", dur=3.4),
    ]
