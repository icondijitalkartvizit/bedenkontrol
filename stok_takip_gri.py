import os
import requests

URL = "https://dunkloss.com/nike-tech-fleece-premium-5th-esofman-alti?renk-seciniz=dark-grey&beden=xxl"
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def check_stock():
    # Şu satırı ekliyoruz ki loglardan görelim token doğru mu gelmiş
    print(f"DEBUG: Token'ın ilk 5 karakteri: {str(BOT_TOKEN)[:5] if BOT_TOKEN else 'BOŞ'}")
    print(f"DEBUG: Chat ID: {CHAT_ID}")
    
    if not BOT_TOKEN or not CHAT_ID:
        print("HATA: Token veya Chat ID yüklenmemiş!")
        return

    # Test mesajı gönderme kısmı
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": "Kirvem test mesajıdır, sistem çalışıyor!"}
    
    response = requests.post(url, data=payload)
    print(f"Telegram Yanıtı: {response.text}")

if __name__ == "__main__":
    check_stock()
    
