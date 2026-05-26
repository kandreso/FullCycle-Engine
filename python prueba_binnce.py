import requests

TELEGRAM_TOKEN = "8702933276:AAEW9h7ia7gaUXrLRo8_gqwtvpbaI5WwDEE"
CHAT_ID = "8409971930"

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mensaje
    }
    requests.post(url, data=data)