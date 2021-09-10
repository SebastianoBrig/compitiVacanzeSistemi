
def main():
   leap = False
   year = int(input("insert the year "))
   if year % 4 == 0:
       if year % 100 == 0:
           if year % 400 == 0:
               leap=True
       else:
           leap=True
           
    
   print(leap)



if __name__ == "__main__":
    main()