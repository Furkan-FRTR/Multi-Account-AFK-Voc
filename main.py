import sys
import json
import time
import requests
import asyncio
import websocket
from flask import Flask
from threading import Thread

app = Flask(__name__)

# CHANNEL_ID est l'identifiant du canal vocal.
GUILD_ID = 35425405805420654204
# CHANNEL_ID est l'identifiant du canal vocal.
CHANNEL_ID = 541654256403052727

# Chemin du fichier contenant les tokens
TOKEN_FILE = 'token.txt'

# Ne pas changer, sauf si vous voulez vous mettre en mode hors ligne, ou désactiver le mode muet et sourdine
# (il est déjà configuré pour être en mode muet et sourdine et en ligne).
SELF_MUTE = True
SELF_DEAF = True
status = "online"

def load_tokens(token_file):
    with open(token_file, 'r') as file:
        tokens = [line.strip() for line in file.readlines()]
    return tokens

def validate_token(token):
    headers = {"Authorization": token, "Content-Type": "application/json"}
    response = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
    if response.status_code != 200:
        print(f"[ERROR] Le token {token} pourrait être invalide. Veuillez le vérifier.")
        return None
    return response.json()

def joiner(token, status):
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    auth = {
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": "Windows 10",
                "$browser": "Google Chrome",
                "$device": "Windows"
            },
            "presence": {
                "status": status,
                "afk": False
            }
        },
        "s": None,
        "t": None
    }
    vc = {
        "op": 4,
        "d": {
            "guild_id": GUILD_ID,
            "channel_id": CHANNEL_ID,
            "self_mute": SELF_MUTE,
            "self_deaf": SELF_DEAF
        }
    }
    ws.send(json.dumps(auth))
    ws.send(json.dumps(vc))
    while True:
        time.sleep(heartbeat / 1000)
        ws.send(json.dumps({"op": 1, "d": None}))

def run_joiner(token):
    userinfo = validate_token(token)
    if userinfo:
        username = userinfo["username"]
        discriminator = userinfo["discriminator"]
        userid = userinfo["id"]
        print(f"Connecté en tant que {username}#{discriminator} ({userid}) avec le token {token}.")
        joiner(token, status)

def start_joiners(tokens):
    threads = []
    for token in tokens:
        t = Thread(target=run_joiner, args=(token,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    tokens = load_tokens(TOKEN_FILE)
    keep_alive()
    start_joiners(tokens)
