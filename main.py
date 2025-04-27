import string 
import random
import os

if not os.path.isfile('.user_settings'):
    mode_password = int(input('''Выберите режим: 
    1 - Только заглавные английские буквы
    2 - Заглавные и прописные английские буквы
    3 - Цифры от 0 до 9
    4 - Цифры и строчные буквы
    5 - Цифры и буквы
    6 - Цыфры и спец символы (!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)
    7 - Цифры, буквы, спец символы: \n'''))
    lenght_password = int(input('Введите длину пароля: \n'))
    hash = int(input('Нужно ли хешировать пароли: 0 - нет; 1 - да: \n'))

    with open('.user_settings', 'w') as f:
        f.write(f"{mode_password}\n")
        f.write(f"{lenght_password}\n")
        f.write(f"{hash}\n")
    

with open('.user_settings', 'r') as f:
    lines_not_remaked = f.readlines()
    line = [i.replace('\n', '') for i in lines_not_remaked]

mode = int(line[0])
lenght_password = int(line[1])
hash = int(line[2])

password = list()

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
else:
    charapters = ''

for i in range(lenght_password):
    password.append(random.choice(list(charapters)))

print(password)
