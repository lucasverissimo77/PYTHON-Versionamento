#Sistema de Mensagens Automáticas
#Feito por Lucas do Verissimo
#V1.0.0.0
import pyautogui as py
import random
import time

# Tempo inicial para abrir o chat
time.sleep(5)

mensagens = [
    "Tá doido?",
    "Mensagem automática",
    "Sistema de mensagens automáticas!",
    "Você é muito burro",
    "20+20+20+7 é muito fácil, professora: é 67",
    "5+5+5+5 é muito fácil, professor!"
]

for i in range(50):
    msg = random.choice(mensagens)
    # Corrige letras e acentos
    msg = msg.strip()
    py.write(msg, interval=0.15)  # digita mais devagar, 0.15s por caractere
    py.press("Enter")
    print(f"Mensagem {i+1}/50 enviada: {msg}")
    time.sleep(random.uniform(0.4, 0.9))  # espera curta e variável
