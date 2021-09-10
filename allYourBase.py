def main():
    list = []
    res = ""
    num = input("insert a number ")
    a = input("insert its base ")
    b = int(input("insert the base to convert it to "))
    c = len(num)-1
    decimal = 0
    for n in num:
        decimal+=int(n) * pow(int(a),c)
        c=c-1
    while decimal != 0:
        list.append(decimal % b)
        decimal = int(decimal / b)
    for k in range(len(list)-1,-1,-1):
        res+=str(list[k])
    print(res)



if __name__ == "__main__":
    main()