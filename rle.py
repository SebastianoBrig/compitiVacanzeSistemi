
def main():
    code = input("insert a string ")
    n=0
    sum=0
    res=""
    for digit in code:
        if n==0:
            ch = digit
            sum+=1
            n+=1
        else:
            if digit==ch:
                sum+=1
            else:
                res+=str(sum) + ch
                sum = 1
                ch = digit
    res+=str(sum) + ch
    print(res)







if __name__=="__main__":
    main()