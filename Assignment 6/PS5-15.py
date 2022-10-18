# Numeric get input
def getInputNum(message):
    a = input(message)
    if a.isnumeric():
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)

y = getInputNum("Please enter a Year: ")

i = y%12
s=""
if i == 8:
    s = "Dragon"
elif i == 9:
    s = "Snake"
elif i == 10:
    s = "Horse"
elif i == 11:
    s = "Sheep"
elif i == 0:
    s = "Monkey"
elif i == 1:
    s = "Rooster"
elif i == 2:
    s = "Dog"
elif i == 3:
    s = "Pig"
elif i == 4:
    s = "Rat"
elif i == 5:
    s = "Ox"
elif i == 6:
    s = "Tiger"
elif i == 7:
    s = "Hare"

print(f"{y} is the year of the {s}")