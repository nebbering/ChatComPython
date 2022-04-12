import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

init()

colors = [Fore.BLUE, Fore.YELLOW, Fore.LIGHTMAGENTA_EX]

client_color = random.choice(colors)

from threading import Thread


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"

s = socket.socket()
print(f"[*] Connection to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Conectado.")

name = input("Digite seu nome:")

def listen_for_messeges():
    while True:
        message = s.recov(1024).decode()
        print("\n" + message)

        t = Thread(target=listen_for_messeges)
        t.daemon = True
        t.start()

while True:
    to_send = input()

    if to_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
    s.send(to_send.encode())
s.close()