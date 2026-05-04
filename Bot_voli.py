import requests
import time
from datetime import datetime

API_KEY = "METTI_API_KIWI"
TELEGRAM_TOKEN = "METTI_TOKEN"
CHAT_ID = "686858158"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check_flights():
    url = "https://api.tequila.kiwi.com/v2/search"
    headers = {"apikey": API_KEY}

    params = {
        "fly_from": "SUF",
        "fly_to": "PSA",
        "date_from": "28/08/2026",
        "date_to": "28/08/2026",
        "curr": "EUR",
        "price_to": 30,
        "limit": 2
    }

    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    if data.get("data"):
        for f in data["data"]:
            msg = f"🔥 Volo a {f['price']}€\n{f['deep_link']}"
            send_telegram(msg)
            print("Inviato!")
    else:
        print(datetime.now(), "Niente voli")

while True:
    check_flights()
    time.sleep(300)
