

def main():
    dizionario = {'a':'z', 'b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h',
    't':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}
    tmp= input("insert the message ")
    message = tmp.lower()
    res=""
    for i in message:
        if i == ' ':
            res+=' '
        else:
            res+=dizionario[i]
    print(res)





if __name__=="__main__":
    main()