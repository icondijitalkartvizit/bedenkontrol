import os
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
        
        # Sayfada Tükendi yazısı varsa dur, yoksa müjdeyi ver
        if "Tükendi" in html or "out-of-stock" in html.lower():
            print("Siyah XXL beden hâlâ stokta yok.")
            return

        if "XXL" in html:
            send_telegram(f"🔥 MÜJDE KİRVE! Siyah Nike Tech XXL Beden Stoğa Girdi!\n\nHemen al: {URL}")
        else:
            print("XXL seçeneği bulunamadı.")
            
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    check_stock()
    
