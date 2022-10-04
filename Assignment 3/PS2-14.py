inToCm = 2.54

ft = int(input("Height (feet): "))
inch = int(input("Height (inches): "))

inch += ft*12

cm = inch*inToCm

print(f"{ft} feet {inch-(ft*12)} inches is {cm} Centimeters")