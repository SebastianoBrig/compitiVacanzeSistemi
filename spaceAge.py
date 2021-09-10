

def main():
    sec = int(input("insert how much seconds is old "))
    ey = sec/31557600

    print(f"earth: {ey}\n mercury: {ey/0.2408467}\n venus: {ey/0.61519726}\n mars: {ey/1.8808158}\n jupiter: {11.862615}\n saturn: {ey/29.447498}\n uranus: {ey/84.016846}\n neptune: {ey/164.79132}")




if __name__=="__main__":
    main()