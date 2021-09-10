

def main():
    stringa=""
    n = int(input("inserisci un numero "))
    if (n % 3) == 0:
        stringa = stringa + "Pling"
    if (n % 5) == 0:
        stringa = stringa + "Plang"
    if (n % 7) == 0:
        stringa = stringa + "Plong"
    print(stringa)



if __name__ == "__main__":
    main()