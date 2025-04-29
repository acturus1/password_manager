from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import questionary
import csv

def registration():
    master = questionary.text("Введите мастер пароль").ask()

    key_for_file = Fernet.generate_key()

    salt = os.urandom(16)

    with open('salt.txt', 'wb') as f:
        f.write(salt)

    def derive_key(password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(), 
            length=32,                
            salt=salt,               
            iterations=100_000,     
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    key = derive_key(master, salt)

    fernet = Fernet(key)

    master = fernet.encrypt(master.encode())

    key_for_file = fernet.encrypt(key_for_file)

    with open('password.txt', 'wb') as f:
        f.write(master + b'\n' + key_for_file)

    headers = [
        "url", 
        "username", 
        "password", 
        "httpRealm", 
        "formActionOrigin", 
        "timeCreated", 
        "timeLastUsed", 
        "timePasswordChanged"
    ]

    with open('password.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        
        # Записываем заголовки
        writer.writerow(headers)

