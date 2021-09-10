
def main():
    num = int(input("insert a number: "))
    lista = []
    k=2
    while num>1:
        if num % k ==0:
            lista.append(k)
            num = num / k
        else: 
            k+=1
    print(lista)
    





if __name__=="__main__":
    main()