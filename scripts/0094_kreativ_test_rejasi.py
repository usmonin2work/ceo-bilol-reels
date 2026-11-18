from lib import *

CAPTION = "Qaysi reklama ishlashini taxmin qilmaymiz — biznesingiz uchun aniq kreativ test rejasini tuzib beramiz."

SUB = "Direct'ga yozing — bepul audit"
BTN = "«TARGET» deb yozing"
M = "* misol uchun, reja biznesingizga bog'liq"

def scenes():
    return [
        T_hook("KREATIV TEST REJASI", [("Qaysi reklama", WHITE, 96, 0), ("ishlashini", GREY, 90, 0),
               ("taxmin qilasizmi?", LIME, 116, 1)], chart=("Byudjet", "↓")),
        T_flow("Reja qanday tuziladi", [("1-hafta", "3 xil hook sinovi", VIO),
               ("2-hafta", "Eng yaxshisiga 3 format", BLUE),
               ("3-hafta", "G'olibga byudjet", TEAL),
               ("natija", "Arzonroq ariza", LIME)], footnote=M, dur=6.0),
        T_list("Biz nima beramiz", [("Test ro'yxati", "nimani, qachon sinash"),
               ("Byudjet", "har testga qancha pul"),
               ("Mezon", "g'olibni raqam aniqlaydi")], marker="check", dur=5.2),
        T_cta("Test rejangizni", "birga tuzamiz.", SUB, BTN, "bepul audit", dur=3.4),
    ]
