import string

def main():
    tmp = input("insert a messagge ")
    message = tmp.lower()
    key = int(input("insert the key "))
    chars = string.ascii_lowercase
    res = ""
    for i in message:
        if i == ' ':
            res+=' '
        else:
            new_i = (chars.index(i)+key) % 26
            res+=chars[new_i]
    print(res)




if __name__=="__main__":
    main()