

def main():
    cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
    c = set(cons)
    w = input("insert a word  ")
    word = w.lower()
    res = ""
    if word[0] == 'a'or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        res=word+"ay"
    if (word[0] == 'x' and word[1] == 'r') or (word[0] == 'y' and word[1] == 't'):
        res=word+"ay"
    if c.issubset(word[0]):
        if word[1] == 'h' or word[1] == 'q':
            res = word+word[0]+word[1]+"ay"
        else:
            res = word+word[0] + "ay"
    print(res)
if __name__=="__main__":
    main()