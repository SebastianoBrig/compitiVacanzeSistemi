
def main():
    c = input("insert the credit card number ")
    card = c.replace(' ','')
    cardlist = []
    for el in card:
        cardlist.append(int(el))
    for i in range(0,len(cardlist)):
        if ((i % 2) == 0):
            new = cardlist[i] * 2
            if new > 9:
                new = new - 9
            cardlist[i] = new
    sum = 0
    for number in cardlist:
        sum+=number
    if sum % 10 == 0:
        print("valid")
    else:
        print("not valid")



if __name__ == "__main__":
    main()