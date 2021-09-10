
def main():
    lista = []
    w = input("Insert the word ")
    n = int(input("insert the number of words "))
    for _ in range(0,n):
        lista.append(input("insert a word "))
    word = set(w)

    for element in lista:
        if word.issubset(set(element)) and len(w)==len(element):
            print(element)




if __name__=="__main__":
    main()