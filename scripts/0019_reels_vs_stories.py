from lib import *

CAPTION = "Reels va Stories reklamasi turli maqsadlar uchun ishlaydi."

def scenes():
    return [
        T_hook("REELS YOKI STORIES?", [("Bir xil video,", WHITE, 100, 0), ("ikki xil joy —", GREY, 90, 0),
               ("qayerga qo'yish kerak?", LIME, 100, 1)]),
        T_vs("Joylashuv farqi",
             {"title": "Reels", "color": BLUE, "rows": [("Maqsad", "tanilish"), ("Tomosha", "uzunroq"), ("Kuchi", "qamrov")]},
             {"title": "Stories", "color": LIME, "rows": [("Maqsad", "harakat"), ("Tomosha", "qisqa"), ("Kuchi", "klik, ariza")]},
             ["Joy emas,", "maqsad tanlovni belgilaydi"], dur=6.0),
        T_list("Qachon nimani tanlash", [("Reels", "yangi auditoriyaga tanishtirish"),
               ("Stories", "aksiya, chegirma, tez ariza"), ("Ikkalasi", "har joyga alohida kreativ")],
               marker="check", dur=4.8),
        T_cta("Joylashuvni", "to'g'ri tanlang.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
