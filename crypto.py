import math

def main():
    lista = []
    tmp = input("insert the message: ")
    message = tmp.replace(' ','')
    c = int(math.sqrt(len(message)))
    r = c
    while r*c < len(message):
        if c+1-r<=1:
            c+=1
        else:
            r+=1
    print(r,c)
    
    

        
    






if __name__ == "__main__":
    main()