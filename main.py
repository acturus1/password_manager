import string 
import random


password = list()

charapters = string.ascii_letters + string.digits
for i in range(10):
    password.append(random.choice(list(charapters)))


print(password)
