dict = {"G":"C","C":"G","T":"A","A":"U"}
def main():
    dna = input("input a dna strand ")
    rna=""
    for nuc in dna:
        rna+=dict[nuc.upper()]
    print(rna)



if __name__ == "__main__":
    main()