dices = []
dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
def main():
    def numbers(n):
        score=0
        for value in dices:
              if value == n:
                  score+=n
        print(score)
    

    for n in range(0,5):
        dices.append(int(input(f"insert the value of the dice n.{n} ")))
    tmp = input("insert the category ")
    category = tmp.lower()

    if category == "ones":
        numbers(1)
    if category == "twos":
        numbers(2)
    if category == "threes":
        numbers(3)
    if category == "fours":
        numbers(4)
    if category == "fives":
        numbers(5)
    if category == "sixes":
        numbers(6)

    if category == "full house":
        sum = 0
        cnt3 = 0
        cnt2 = 0
        for value in dices:
            sum+=value
            dict[value]+=1
        for element in dict:
            if element==3:
                cnt3 +=1
            if element==2:
                cnt2 += 1      
        if cnt3 == 1 and cnt2 == 1:
            print(sum)
        else:
            print(0)
        
    if category == "four of a kind":
        cnt = 0
        score = 0
        for value in dices:
            dict[value]+=1
        k=1
        for element in dict:
            if element==4:
                score = 4*k
                cnt = 1
            k=k+1
        if cnt == 1:
            print(score)
        else:
            print(0)
        
    if category == "little straight":
        tmp = [1,2,3,4,5]
        pool = set(tmp)
        if pool.issubset(dices) == True:
            print(30)
        else:
            print(0)

    if category == "big straight":
        tmp = [2,3,4,5,6]
        pool = set(tmp)
        if pool.issubset(dices):
            print(30)
        else:
            print(0)
    
    if category == "choice":
        score=0
        for value in dices:
            score+=value
        print(score)
    
    if category == "yatch":
        if dices[0] == dices[1] and dices[0] == dices[2] and dices[0] == dices[3] and dices[0] == dices[4]:
            print(50)
        else:
            print(0)





if __name__=="__main__":
    main()