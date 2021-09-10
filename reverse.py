
def main():
    revString=""
    string = input("insert a string ")
    for n in range(len(string)-1,-1,-1):
        revString+=string[n]
    print(revString)

if __name__ == "__main__":
    main()