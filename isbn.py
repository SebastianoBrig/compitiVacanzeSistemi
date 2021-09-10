
def main():
    tmp = input("insert the isbn code ")
    isbn = tmp.replace("-","")
    c=10
    sum=0
    for digit in isbn:
        if digit == 'X':
            sum+=10 * c
        else:
            sum+=int(digit)*c
        c=c-1
    res = sum % 11
    if res==0:
        print("valid")
    else:
        print("not valid")
    


if __name__=="__main__":
    main()