import string 
import random
import os

if not os.path.isfile('.user_settings'):
    mode_password = input('''Введите режим: 
    1 - Только заглавные английские буквы
    2 - Заглавные и прописные английские буквы
    3 - Все что в пунктах выше + спец символы: \n''')
    lenght_password = input('Введите длину пароля: \n')
    hash = input('Нужно ли хешировать пароли: 0 - нет; 1 - да: \n')

    with open('.user_settings', 'w') as f:
        f.write(f"{mode_password}\n")
        f.write(f"{lenght_password}\n")
        f.write(f"{hash}\n")
    

with open('.user_settings', 'r') as f:
    lines_not_remaked = f.readlines()
    line = [i.replace('\n', '') for i in lines_not_remaked]

mode = line[0]
lenght_password = line[1]
hash = line[2]

password = list()



charapters = string.ascii_letters + string.digits
for i in range(10):
    password.append(random.choice(list(charapters)))

print(password)
