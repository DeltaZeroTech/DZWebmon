import os
import requests
import time
import difflib
from telegram import Bot
from telegram.error import TelegramError
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise ValueError("Le BOT_TOKEN ou le CHAT_ID est manquant dans le fichier .env.")

def split_message(message, max_length=4096):
    return [message[i:i + max_length] for i in range(0, len(message), max_length)]

def send_telegram_notification(bot_token, chat_id, url, changes):
    try:
        bot = Bot(token=bot_token)
        message = f"Changements détectés sur {url} :\n" + "\n".join(changes)
        
        parts = split_message(message)

        for part in parts:
            bot.send_message(chat_id=chat_id, text=part)
        
        print(f"Notification envoyée avec succès à {chat_id}.")
    except TelegramError as e:
        print(f"Erreur lors de l'envoi de la notification Telegram : {e}")

def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.text
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        return None

def compare_content(old_content, new_content):
    diff = difflib.unified_diff(
        old_content.splitlines(), new_content.splitlines(), lineterm='', n=0
    )
    return list(diff)

def save_changes_to_file(url, changes):
    filename = f"changes_{url.replace('https://', '').replace('/', '_')}.txt"
    with open(filename, "a", encoding='utf-8') as file:
        file.write("\n".join(changes))
        file.write("\n---\n")  

def monitor_page(url, interval=60):
    print(f"Surveillance de la page : {url}")
    old_content = fetch_page_content(url)
    
    if old_content is None:
        print(f"Impossible de récupérer le contenu initial de la page {url}.")
        return
    
    while True:
        time.sleep(interval)
        new_content = fetch_page_content(url)
        
        if new_content is None:
            continue
        
        changes = compare_content(old_content, new_content)
        
        if changes:
            print(f"Changements détectés sur {url} !")
            for line in changes:
                print(line)
            
            send_telegram_notification(BOT_TOKEN, CHAT_ID, url, changes)
            
            save_changes_to_file(url, changes)
            
            old_content = new_content
        else:
            print(f"Aucun changement sur {url}")

# URL de la page à surveiller
url = "https://exemple.com"

# Surveillance de la page toutes les 60s par défaut
monitor_page(url, interval=60)
