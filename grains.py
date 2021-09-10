
def main():
    sq = int(input("insert the number of the square: "))
    lista = []
    k = 1
    lista.append(k)
    sum = 1
    for _ in range(1,64):
        k=k*2
        sum+=k
        lista.append(k)
    print(lista[sq-1])
    print(sum)



if __name__=="__main__":
    main()