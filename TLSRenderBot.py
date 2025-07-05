import time
import requests
import telegram

BOT_TOKEN = "7854652580:AAHw0N4fzoqQJehtyfrxb3Hjz8-s-BFjmpk"
CHAT_ID = "6682856752"

def check_tls():
    url = "https://fr.tlscontact.com/appointment/ma/maRBA2fr/20230581"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if "Aucun rendez-vous" not in response.text:
            send_telegram("✅ Nouveau créneau détecté !")
        else:
            print("⏳ Aucun créneau...")
    except Exception as e:
        print("⚠️ Erreur :", e)

def send_telegram(message):
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    while True:
        check_tls()
        time.sleep(300)  # toutes les 5 minutes
