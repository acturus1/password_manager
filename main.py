import string 
import random
import os
import questionary
import sqlite3

con = sqlite3.connect('passwords.db')

db = con.cursor()

db.execute('''CREATE TABLE IF NOT EXISTS passwords(sait, password)''')

def is_int(text):
    return text.isdigit() or "Пожалуйста, введите целое число"

if not os.path.isfile('.user_settings'):
    mode_password = questionary.select('Выберите режим:',
    [
        '1 - Только заглавные английские буквы',
        '2 - Заглавные и прописные английские буквы',
        '3 - Цифры от 0 до 9',
        '4 - Цифры и строчные буквы',
        '5 - Цифры и буквы',
        '''6 - Цыфры и спец символы (!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)''',
        '7 - Цифры, буквы, спец символы'''
    ]).ask()
    mode_password = mode_password[:1]
    lenght_password = questionary.text('Введите длину пароля:', validate=is_int).ask()
    hash = questionary.confirm('Нужно ли хешировать пароли:').ask()
    with open('.user_settings', 'w') as f:
        f.write(f"{mode_password}\n")
        f.write(f"{lenght_password}\n")
        f.write(f"{hash}\n")
    
with open('.user_settings', 'r') as f:
    lines_not_remaked = f.readlines()
    line = [i.replace('\n', '') for i in lines_not_remaked]

mode = int(line[0])
lenght_password = int(line[1])
hash = bool(line[2])

password = ''

if mode == 1:
    charapters = string.ascii_lowercase
elif mode == 2:
    charapters = string.ascii_letters
elif mode == 3:
    charapters = string.digits
elif mode == 4:
    charapters = string.ascii_lowercase + string.digits
elif mode == 5:
    charapters = string.ascii_letters + string.digits
elif mode == 6:
    charapters = string.digits + string.punctuation
elif mode == 7:
    charapters = string.ascii_letters + string.digits + string.punctuation


sait = questionary.text('Введите имя сайта для которого предназначется этот пароль').ask()   

for i in range(lenght_password):
    password += random.choice(list(charapters))

print(f"{sait} - {password}")
