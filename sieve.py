
def main():
    dizionario = {}
    limit = int(input("insert the limit "))

    for i in range(2,limit+1):
        dizionario[i]=0
    for num,mark in dizionario.items():
        if mark == 0:
            for a,b in dizionario.items():
                if a % num == 0 and a!=num:
                    dizionario[a] = 1
    print(f"prime numbers in range (2, {limit}) :")
    for num,mark in dizionario.items():
        if mark == 0:
            print(num)






if __name__=="__main__":
    main()