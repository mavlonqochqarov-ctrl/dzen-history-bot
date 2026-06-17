#!/usr/bin/env python3
"""
Dzen Tarix/Faktlar maqola generatori (Gemini API)
Har kuni avtomatik yangi maqola + rasm generatsiya qiladi
"""

import json
import random
import os
from datetime import datetime
from pathlib import Path
from google import genai
from google.genai import types

# Gemini API kalitini o'rnating (GitHub Secrets dan olinadi)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def load_topics():
    """Mavzular ro'yxatini yuklaydi"""
    topics_file = Path(__file__).parent.parent / "topics.json"
    with open(topics_file, "r", encoding="utf-8") as f:
        return json.load(f)

def select_topic(topics_data):
    """Tasodifiy mavzu tanlaydi"""
    categories = topics_data["categories"]
    category = random.choice(categories)
    topic = random.choice(category["topics"])
    return category["name"], category["emoji"], topic

def generate_article_prompt(category_name, emoji, topic):
    """AI uchun maqola prompti"""
    return f"""Sen professional tarixiy maqola yozuvchisan. Quyidagi mavzuda Dzen platformasi uchun maqola yoz:

MOVZU: {emoji} {topic}

TALABLAR:
1. Maqola 800-1200 so'zdan iborat bo'lsin
2. Sarlavha qiziqarli va diqqatni tortuvchi bo'lsin
3. Har bir paragrafda faktlar va raqamlar bo'lsin
4. Oxirida "Siz buning oldin bilasizmi?" yoki shunga o'xshash savol qo'yil
5. Matn oson tushunarli, qiziqarli va tarbiyaviy bo'lsin
6. Emoji lardan foydalan (lekin ortiqcha emas)
7. SEO uchun kalit so'zlar kiriting
8. Har bir bo'lim uchun rasm tavsifini qo'sh (rasm uchun)

FORMAT:
# [SARLAVA]

[MATN]

---
📌 Siz bilasizmi? [qiziqarli fakt]

[RASM TAVSIFI: rasm uchun tavsif]

#tarix #faktlar #qiziqarli #tarixiy #maqola

MAQOLA MATNI:"""

def generate_image_prompt(topic, article_text):
    """Rasm uchun prompt yaratadi"""
    return f"""Generate a historically accurate, visually appealing illustration for this topic: {topic}

The image should be:
- Professional and educational style
- Suitable for a history/facts article
- High quality and detailed
- Appropriate for social media sharing

Topic context: {article_text[:500]}

Style: Digital illustration, warm colors, historical atmosphere"""

def call_gemini_api(prompt):
    """Gemini API ni chaqiradi (matn)"""
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    return response.text

def generate_image(topic, article_text):
    """Gemini API orqali rasm generatsiya qiladi"""
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        image_prompt = generate_image_prompt(topic, article_text)
        
        response = client.models.generate_images(
            model="imagen-3.0-generate-002",
            prompt=image_prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
            )
        )
        
        return response.generated_images[0].image.image_bytes
        
    except Exception as e:
        print(f"⚠️ Rasm generatsiya qilishda xatolik: {e}")
        return None

def save_article(article_text, topic, category_name, image_bytes=None):
    """Maqolani faylga saqlaydi"""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-{category_name}.md"
    filepath = Path(__file__).parent.parent / "articles" / filename
    
    # Rasmni saqlash
    image_filename = None
    if image_bytes:
        image_filename = f"{today}-{category_name}.png"
        image_path = Path(__file__).parent.parent / "articles" / image_filename
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        print(f"🖼️ Rasm saqlandi: {image_filename}")

    # Maqolaning to'liq kontentini yaratadi
    full_content = f"""---
date: {today}
category: {category_name}
topic: {topic}
status: draft
platform: dzen
image: {image_filename}
---

{article_text}
"""
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    return filepath, image_filename

def main():
    """Asosiy funksiya"""
    print("🤖 Dzen maqola generatori (Gemini API) ishga tushdi...")
    
    # API kalitini tekshirish
    if not GEMINI_API_KEY:
        print("❌ GEMINI_API_KEY topilmadi!")
        print("GitHub repo > Settings > Secrets > Actions ga qo'shing.")
        print("API kalitini olish: https://aistudio.google.com/apikey")
        return
    
    # Mavzularni yuklash
    topics_data = load_topics()
    
    # Mavzu tanlash
    category_name, emoji, topic = select_topic(topics_data)
    print(f"📝 Tanlangan mavzu: {emoji} {topic}")
    
    # Maqola prompti yaratish
    article_prompt = generate_article_prompt(category_name, emoji, topic)
    
    # Gemini API ni chaqirish (matn)
    try:
        print("⏳ Maqola yaratilmoqda...")
        article = call_gemini_api(article_prompt)
        print("✅ Maqola yaratildi!")
        
    except Exception as e:
        print(f"❌ Maqola yaratishda xatolik: {e}")
        return
    
    # Rasm generatsiya qilish
    print("🖼️ Rasm yaratilmoqda...")
    image_bytes = generate_image(topic, article)
    
    # Maqolani saqlash
    filepath, image_filename = save_article(article, topic, category_name, image_bytes)
    
    print(f"✅ Maqola saqlandi: {filepath}")
    if image_filename:
        print(f"🖼️ Rasm: {image_filename}")
    print(f"📄 Fayl: {filepath.name}")

if __name__ == "__main__":
    main()
