from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import questionary
import ast
from session import session

def login():
    if session.check_session():
        print('session')

    elif not session.check_session():
        login = questionary.text('Введите ваш мастер пароль').ask()

        def derive_key(password, salt):
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(), 
                length=32,                
                salt=salt,               
                iterations=100_000,     
            )
            key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
            return key

        with open('salt.txt', 'rb') as f:
            salt = f.read()
            
        key = derive_key(login, salt)

        fernet = Fernet(key)

        with open('password.txt', 'rb') as f:
            lines = f.read().split(b'\n')
            encrypted_master = lines[0]
            encrypted_key_for_file = lines[1]

        master = fernet.decrypt(encrypted_master).decode()
        key_for_file = fernet.decrypt(encrypted_key_for_file).decode()

        print(master, key_for_file)

        session.create_session()

if __name__ == "__main__":  
    login()
