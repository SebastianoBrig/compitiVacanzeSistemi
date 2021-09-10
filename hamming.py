

def main():
    str1 = input("insert the first strands of DNA ")
    str2 = input("insert the second strands of DNA ")
    hammingdistance = 0
    for a,b in zip(str1,str2):
        if a != b:
            hammingdistance=hammingdistance+1
    print(f"the hamming distance is {hammingdistance}")

    



if __name__ == "__main__":
    main()

