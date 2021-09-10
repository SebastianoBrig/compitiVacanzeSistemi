
def main():
    w = input("insert a word ")
    wo =w.replace(' ','')
    word = wo.replace('-','')
    iso = 0
    for letter in word:
        for l in range(0,len(word)):
            if letter == word[l]:
                iso = iso+1
    if iso > len(word):
        print("the word isn't an isogram")
    else:
        print("the word is an isogram")



if __name__=="__main__":
    main()