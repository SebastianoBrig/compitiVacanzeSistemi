dizionario = {}
def main():
   file = open("./tournament.csv", "r")
   read(file)
   output = "Team                           | MP |  W |  D |  L |  P\n"
   for team in dizionario:
       output=output+team[0]+"| "+team[1] + "| "+ team[2] + "| "+team[3]+ "| "+team[4]+"| "+team[5]+"\n"
   print(output)

def read(file):
    for riga in file:
        match = riga.split(';')
        print(match)
        if match[2] == 'win':
            print("a")
            dizionario[match[0]][2]+=1
            dizionario[match[0]][5]+=3
            dizionario[match[1]][4]+=1

        if match[2] == "loss":
            print("b")
            dizionario[match[0]][4]+=1
            dizionario[match[1]][2]+=1
            dizionario[match[1]][5]+=3

        if match[2] == "draw":
            print("c")
            dizionario[match[0]][3]+=1
            dizionario[match[0]][5]+=1
            dizionario[match[1]][3]+=1
            dizionario[match[1]][5]+=1
        dizionario[match[0]][0] = match[0]
        dizionario[match[1]][0] = match[1]
        dizionario[match[0]][1]+=1
        dizionario[match[1]][1]+=1

    

            
        
if __name__ == "__main__":
    main()