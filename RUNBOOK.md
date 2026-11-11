# Instagram Reels avtopost — ish tartibi

Akkaunt: **ceo.bilol** (Windsor.ai, connector `instagram`, account `17841474593715307`).
Har bir ishga tushish = **bitta yangi video** tayyorlash va joylash.

## Qoidalar (egasi belgilagan)
- Faqat **yangi** videolar. Oldin joylangan mavzu yoki videoni qayta ishlatmang (`posted.md`).
- Sarlavha (caption) — **bitta qisqa gap, bir qator**. Heshteg, @mention yozilmaydi.
- Vizual uslub va SFX — `engine/` dagi shablonlar, o'zgartirmang. Musiqa qo'yilmaydi, faqat SFX.
- Raqamli misollarda `* misol uchun...` izohi bo'lsin.
- Sotuvchi videolarda CTA: Direct'ga «TARGET» deb yozing — bepul audit.
- Tag (@sadriddin_abdurahimov, @leverage_mentorlik) Windsor orqali qo'yib bo'lmaydi — egasi qo'lda qo'shadi.

## Qadamlar
1. `topics.md` dan birinchi `[ ]` mavzuni oling.
2. `scripts/_example.py` ni namuna qilib `scripts/NNNN_qisqa_nom.py` yozing (NNNN = `posted.md` dagi oxirgi raqam + 1).
   4–5 sahna: hook → 2–3 asosiy sahna → CTA. Matnlar o'zbekcha (lotin), qisqa.
3. `python3 engine/make.py scripts/NNNN_....py --stills` — `videos/NNNN_..._preview.png` ni oching, matn sig'ishini tekshiring.
4. `python3 engine/make.py scripts/NNNN_....py` — `videos/NNNN_....mp4`.
5. `git add scripts videos topics.md && git commit && git push` (avval `git pull --rebase`).
6. Havola: `https://raw.githubusercontent.com/usmonin2work/ceo-bilol-reels/main/videos/NNNN_....mp4`
   (push'dan keyin `curl -sI` bilan 200 ekanini tekshiring).
7. Windsor `execute_action`: connector `instagram`, action `create_video_post`, account `17841474593715307`,
   params `{video_url, caption: CAPTION, share_to_feed: true}`.
8. `topics.md` da mavzuni `[x]` qiling, `posted.md` ga qator qo'shing: `NNNN | sana-vaqt | fayl | caption | media_id`. Commit + push.
9. Xato bo'lsa (Instagram rad etdi va h.k.) — `posted.md` ga `XATO` bilan yozing va hisobotda ayting.

Eski videolar `videos/` da saqlanadi; repo 1 GB ga yaqinlashsa, 30 kundan eski mp4 larni o'chiring (Instagram ularni allaqachon yuklab olgan).
