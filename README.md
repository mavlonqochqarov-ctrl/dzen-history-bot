# 🤖 Dzen Tarix/Faktlar Bot (Gemini API)

Dzen platformasi uchun avtomatik tarixiy maqolalar + rasm yaratuvchi bot.

## ✨ Imkoniyatlari

- ✅ Har kuni avtomatik yangi maqola generatsiya qiladi
- ✅ **Rasm ham avtomatik yaratiladi** (Imagen 3.0)
- ✅ 8 ta turli kategoriya
- ✅ SEO optimallashtirilgan maqolalar
- ✅ O'zbek tilida yuqori sifatli kontent
- ✅ **BEPUL** (kuniga 15 ta so'rov)

## 🚀 Boshlash

### 1. GitHub Repo yaratish

```bash
# GitHub ga boring va yangi repo yarating
# Nomi: dzen-history-bot
```

### 2. Gemini API kalitini olish

1. https://aistudio.google.com/apikey ga boring
2. Google hisobingiz bilan kiring
3. "Create API Key" bosing
4. API kalitini nusxalang

### 3. API kalitini GitHub ga qo'shish

1. GitHub repo > **Settings**
2. **Secrets and variables** > **Actions**
3. **New repository secret** bosing
4. Name: `GEMINI_API_KEY`
5. Value: API kalitingiz

### 4. Botni ishga tushirish

- Har kuni avtomatik **08:00** (Toshkent vaqti) da ishlaydi
- Yoki **Actions** > **Dzen Maqola Generatori** > **Run workflow** bosing

## 📁 Loyiha tuzilishi

```
dzen-history-bot/
├── articles/                    ← maqolalar + rasmlar saqlanadi
│   ├── 2025-01-15-buyuk_insonlar.md
│   └── 2025-01-15-buyuk_insonlar.png
├── templates/
│   └── article.md              ← maqola shabloni
├── scripts/
│   └── generate.py             ← asosiy skript
├── .github/workflows/
│   └── generate.yml            ← GitHub Actions
├── topics.json                 ← 80+ mavzu
├── requirements.txt
└── README.md
```

## 📝 Mavzular (8 kategoriya)

| # | Kategoriya | Emoji | Namuna mavzu |
|---|------------|-------|--------------|
| 1 | Buyuk insonlar | 👤 | Napoleon qanday qilib Yevropani zabt etdi |
| 2 | Qadimiy sivilizatsiya | 🏛️ | Misr piramidalarining haqiqiy sirlari |
| 3 | Urush tarixi | ⚔️ | Ikkinchi jahon urushidagi sirli operatsiyalar |
| 4 | Geografiya | 🌍 | Dunyodagi eng g'ayrioddiy 10 ta joy |
| 5 | Ilmiy kashfiyotlar | 🔬 | DNA ning kashfiyot tarixi |
| 6 | Sirli hodisalar | 🔮 | Bermuda uchburchagi — haqiqat yoki afsona? |
| 7 | Madaniyat | 🎭 | Mona Lisaning haqiqiy siri |
| 8 | Ovqat tarixi | 🍽️ | Kofe — dunyoni o'zgartirgan ichimlik |

## 💡 Dzen da muvaffaqiyat sirlari

1. **Sarlavha**: Qiziqarli va diqqatni tortuvchi
2. **Rasm**: Har doim rasm qo'shing (bot avtomatik yaratadi)
3. **Faktlar**: Har bir paragrafda faktlar bo'lsin
4. **Emoji**: Joyida emoji ishlating
5. **Savol**: Oxirida savol qo'ying
6. **Hashtag**: #tarix #faktlar kabi hashtaglar
7. **Muntazamlik**: Har kuni bir xil vaqtda joylashtiring

## ⚠️ Muhim eslatmalar

- API kalitini hech qachon ochiq qilmang
- Maqolalarni tekshirib, keyin Dzen ga joylashtiring
- Dzen qoidalarini buzmang
- Plagiatdan saqlaning
- Kuniga 15 ta bepul so'rov (Gemini API limiti)

## 🔧 Qo'shimcha sozlash

### Mavzular qo'shish

`topics.json` faylini tahrirlang:

```json
{
  "categories": [
    {
      "name": "yangi_kategoriya",
      "emoji": "🆕",
      "topics": [
        "Mavzu 1",
        "Mavzu 2"
      ]
    }
  ]
}
```

### Maqola formatini o'zgartirish

`topics.json` da `article_format` bo'limini tahrirlang.

## 📞 Yordam

Savollaringiz bo'lsa, GitHub Issues ga yozing.

---

**Omad tilaymiz! 🚀**
