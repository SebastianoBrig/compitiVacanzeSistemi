import random
lista = []
points = []
max = 0
sum = 0
for i in range(0,6):
    for _ in range(0,4):
        lista.append(random.randint(1,6))
    print(lista)
    for _ in range (0,3):
        for el in lista:
            if el > max:
                max = el
                ind = lista.index(el)
        sum+=max
        lista[ind] = 0
        max = 0
    lista = []
    points.append(sum)
    sum = 0
mod = int((points[2]-10) / 2)
hitpoints=10-mod
print(points,"hitpoints:",hitpoints)