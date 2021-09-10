import string
import random

lista = []
for _ in range(0,100):
    while True:
        name=""
        k=False
        for _ in range(0,2):
            name+=random.choice(string.ascii_uppercase)
        for _ in range(0,3):
            name+=str(random.randint(1,9))
        for el in lista:
            if name == el:
                k=True
        if k == False:
            break
    lista.append(name)
print(lista)