def main():
    stringa = input("inserisci la stringa: ")
    verifica(stringa)

def verifica(stringa):
    ris = True
    pila = []
    for elemento in stringa:
        if elemento == "{" or elemento == "[" or elemento == "(":
            pila.append(elemento)
        if elemento == "}" or elemento == "]" or elemento == ")":
            x = pila.pop()
            if (x=="{" and elemento!="}"):
                ris = False
            if (x=="[" and elemento!="]"):
                ris = False
            if (x=="(" and elemento!=")"):
                ris = False
    if (len(pila)>0):
        ris=False
    if (ris==True):
        print("corretta")
    else:
        print("sbagliata")

if __name__=="__main__":
    main()

    