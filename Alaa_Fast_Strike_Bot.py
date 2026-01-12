import telebot
import shodan
import concurrent.futures
from gtts import gTTS
import os
import time

# ==========================================
# Developed by: Alaa Ahmed
# Project: Ghost-Protocol-GRC (Fast Strike Edition)
# Purpose: High-speed Parallel Security Reconnaissance
# ==========================================

# Configuration - [Keys hidden for security purposes]
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
SHODAN_KEY = "YOUR_SHODAN_API_KEY"
MY_ID = "YOUR_TELEGRAM_ID"

bot = telebot.TeleBot(TOKEN)
api = shodan.Shodan(SHODAN_KEY)

# Strategic Targets for Monitoring
DOMAINS = ["flynas.com", "riyadhart.sa", "rcrc.gov.sa", "moity.gov.sa"]

def send_vocal(text):
    """Generates AI voice notification for critical findings"""
    try:
        tts = gTTS(text=text, lang='ar')
        tts.save("alert.mp3")
        with open("alert.mp3", 'rb') as v:
            bot.send_voice(MY_ID, v)
        os.remove("alert.mp3")
    except Exception as e:
        print(f"Vocal Alert Error: {e}")

def scan_target(domain):
    """Performs high-speed reconnaissance using Shodan API"""
    print(f"🚀 Scanning Target: {domain}")
    try:
        # Searching for exposed ports and services
        query = f"hostname:{domain}"
        results = api.search(query, limit=5)
        for res in results['matches']:
            ip = res['ip_str']
            port = res['port']
            
            # Identify non-standard ports that may require security attention
            if port not in [80, 443]:
                msg = f"Security Alert: Discovery on {domain}. IP: {ip}. Non-standard port {port} detected."
                bot.send_message(MY_ID, f"⚡ [FAST STRIKE] Target Identified!\n📍 IP: {ip}:{port}\n🏢 Entity: {domain}")
                send_vocal(f"تنبيه أمني لآلاء، تم رصد هدف في {domain}")
                
    except shodan.APIError:
        time.sleep(5)
    except Exception:
        pass

def run_fast_mode():
    """Initiates the Parallel Processing Engine"""
    print("🏎️ Alaa's Speed Engine Activated. Running Parallel Mode...")
    while True:
        # Multi-threading for maximum performance
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(scan_target, DOMAINS)
        time.sleep(15) # Optimized interval for continuous scanning

if __name__ == "__main__":
    run_fast_mode()
