def CtoF(cel):
    return (cel*9/5)+32

def CtoK(cel):
    return cel + 273.15

i = float(input("Temperature in Celsius: "))

print(f"{i} degrees Celsius is {CtoF(i)} degrees Fahrenheit and {CtoK(i)} Kelvin")