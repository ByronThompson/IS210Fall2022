def ftToCm(feet, inches):
    inToCm = 2.54
    inches += ft * 12
    return inches * inToCm

ft = int(input("Height (feet): "))
inch = int(input("Height (inches): "))

print(f"{ft} feet {inch} inches is {ftToCm(ft, inch)} Centimeters")