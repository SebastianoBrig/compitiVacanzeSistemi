

def main():
    n = int(input("insert the number of natural numbers "))
    sq_sum=0
    sum_sq=0
    for i in range(1,n+1):
        sq_sum+=i
        sum_sq+=pow(i,2)
    sq_sum=pow(sq_sum,2)
    res = sq_sum-sum_sq
    print(res)



if __name__ == "__main__":
    main()