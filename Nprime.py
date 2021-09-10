

n = int(input("insert the nth prime number you want to know: "))
p=0
num = 1
while p<n:
        num+=1
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            p+=1
print(num)
