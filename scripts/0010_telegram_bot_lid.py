from lib import *

CAPTION = "Telegram botga lid yig'ish qulay, lekin uning ham kamchiliklari bor."

def scenes():
    return [
        T_hook("TELEGRAM BOT", [("Lidni botga", WHITE, 110, 0), ("yig'ish", GREY, 90, 0),
               ("arziydimi?", LIME, 140, 1)]),
        T_vs("Bot orqali lid",
             {"title": "Afzalligi", "color": LIME, "rows": [("Kirish", "bir bosish"), ("Aloqa", "darhol"), ("Qayta yozish", "oson")]},
             {"title": "Kamchiligi", "color": BLUE, "rows": [("Telefon", "har doim emas"), ("Tashlab ketish", "ko'p"), ("Pixel", "ko'rmaydi")]},
             ["Bot qulay,", "lekin natijani o'lchash qiyin"], dur=6.0),
        T_list("Botdan to'g'ri foydalanish", [("Qisqa savollar", "3 tadan oshmasin"),
               ("Telefon so'rang", "kontakt tugmasi bilan"), ("Tez javob", "operator 5 daqiqada yozsin")],
               marker="check", dur=4.8),
        T_cta("Bot — vosita,", "jarayon muhim.", "Foydali bo'lsa, saqlab qo'ying", "Saqlab qo'ying", "va do'stingizga ulashing"),
    ]
