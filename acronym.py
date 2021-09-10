
def main():
    acr = ""
    name = input("insert the name ")
    list = name.split(' ')
    for element in list:
        acr+=element[0]
    print(acr)



if __name__ == "__main__":
    main()