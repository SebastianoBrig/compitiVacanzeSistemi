
def main():
    lista = [5,6,7,11,15,6,99]
    high(lista)
    last(lista)
    highest3(lista)

def high(lista):
    highest=-1
    for score in lista:
        if score>highest:
            highest = score
    print(f"the highest score is {highest}\n")

def last(lista):
    last1 = lista[-1]
    print(f"the last score is {last1}\n")

def highest3(lista):
    highest1=-1
    for score in lista:
        if score>highest1:
            highest1 = score
    highest2 = -1
    for score in lista:
        if score>highest2:
            if score != highest1:
                highest2 = score
    highest3 = -1
    for score in lista:
        if score>highest3:
            if score != highest1 and score != highest2:
                highest3 = score
    
    print(f"the highest 3 score are {highest1} {highest2} {highest3}")


if __name__ == "__main__":
    main()