import os
import re
import requests

URL = "https://dunkloss.com/nike-tech-fleece-premium-5th-esofman-alti?renk-seciniz=black&beden=xxl"
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram(message):
    if BOT_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def check_stock():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(URL, headers=headers, timeout=10)
        html = response.text
        
        # HTML içinde XXL seçeneğinin ve stok durumunun kontrolü
        if "XXL" in html:
            # Sitede tükenmiş butonlarında genelde 'disabled' veya 'out-of-stock' sınıfı olur
            disabled_pattern = r'<[^>]*data-variant[^>]*XXL[^>]*disabled'
            if not re.search(disabled_pattern, html, re.IGNORECASE):
                send_telegram(f"🔥 MÜJDE KİRVE! Nike Tech XXL Beden Stoğa Girdi!\n\nHemen al: {URL}")
            else:
                print("XXL beden hâlâ stokta yok.")
        else:
            print("Sayfa çekildi ancak XXL bedeni doğrulanamadı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    check_stock()
