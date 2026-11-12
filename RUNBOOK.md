# Instagram Reels avtopost — ish tartibi

Akkaunt: **ceo.bilol** (Windsor.ai, connector `instagram`, account `17841474593715307`).
Har bir ishga tushish = **1 ta tayyor videoni joylash** (A), keyin vaqt bo'lsa **zaxiraga 1 ta yangi video** (B).

## Qoidalar (egasi belgilagan)
- Faqat **yangi** videolar. Oldin joylangan mavzu yoki videoni qayta ishlatmang (`posted.md`).
- Sarlavha (caption) — **bitta qisqa gap, bir qator**. Heshteg, @mention yozilmaydi.
- Vizual uslub va SFX — `engine/` dagi shablonlar, o'zgartirmang. Musiqa qo'yilmaydi, faqat SFX.
- Raqamli misollarda `* misol uchun...` izohi bo'lsin. Sotuvchi videolarda CTA: Direct'ga «TARGET» deb yozing — bepul audit.
- Tag (@sadriddin_abdurahimov, @leverage_mentorlik) Windsor orqali qo'yib bo'lmaydi — egasi qo'lda qo'shadi.

## MUHIM: ishni yarim yo'lda tashlamang
- Avvalgi ishga tushishlar ~1 daqiqada, hech narsa joylamasdan tugagan. Shuning uchun ENG AVVAL joylash (A) qilinadi —
  u faqat clone + bitta Windsor chaqiruvi.
- Biror buyruq yoki tool "moved to the background" desa — uning tugash xabarini kuting, keyin davom eting.
  A bajarilmaguncha (yoki XATO yozilmaguncha) yakuniy javob yozmang.

## A. Tayyor videoni joylash (har safar, birinchi bo'lib)
1. `ready.md` dagi BIRINCHI qatorni oling: `fayl | caption`.
   - `ready.md` bo'sh bo'lsa: B ni bajaring (yangi video yasang), keyin shu videoni joylang.
2. Windsor `execute_action`: connector `instagram`, action `create_video_post`, account `17841474593715307`,
   params `{"video_url": "https://raw.githubusercontent.com/usmonin2work/ceo-bilol-reels/main/videos/<fayl>", "caption": "<caption>", "share_to_feed": true}`.
3. Muvaffaqiyatli bo'lsa: o'sha qatorni `ready.md` dan o'chiring, `posted.md` ga qo'shing
   (`NNNN | sana-vaqt Toshkent | fayl | caption | media_id`), `git rm videos/<fayl>` (Instagram allaqachon yuklab olgan, repo kichik qoladi).
   `git pull --rebase && git commit && git push`.
4. Xato bo'lsa: `posted.md` ga `XATO` bilan yozing, qatorni `ready.md` da qoldiring, push qiling.

## B. Zaxiraga yangi video (faqat `ready.md` da 5 tadan kam qolgan bo'lsa)
1. `topics.md` dan birinchi `[ ]` mavzu. `scripts/_example.py` namunasida `scripts/NNNN_qisqa_nom.py` yozing
   (NNNN = scripts/ dagi eng katta raqam + 1). 4 sahna: hook → 2 asosiy sahna → CTA. Matnlar o'zbekcha (lotin), qisqa.
2. `python3 engine/make.py scripts/NNNN_....py --stills` → `videos/NNNN_..._preview.png` ni Read bilan ko'ring, matn sig'ishini tekshiring.
3. `python3 engine/make.py scripts/NNNN_....py` (~30–60 s, timeout 600000).
4. `ready.md` oxiriga `NNNN_....mp4 | CAPTION` qo'shing, `topics.md` da `[x]`. Preview png ni o'chiring. Commit + push.
5. `topics.md` da 10 tadan kam bo'sh mavzu qolsa — oxiriga 30 ta yangi, takrorlanmaydigan mavzu qo'shing (har 3-chisi S).
