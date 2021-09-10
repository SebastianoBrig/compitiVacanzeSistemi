

def main():
    num = input("insert a number ")
    sum = 0
    k = len(num)
    for digit in num:
        sum+=pow(int(digit),k)
    if sum == int(num):
        print("is an armstrong number")
    else:
        print("is not an armstrong number")




if __name__ == "__main__":
    main()