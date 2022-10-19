# Numeric get input
def getInputNum(message):
    a = input(message)
    if a.isnumeric():
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)

s = getInputNum("Please enter the number of sides a shape has: ")

if s == 3:
    print("That is a triangle")
elif s == 4:
    print("That is a square")
elif s == 5:
    print("That is a pentagon")
elif s == 6:
    print("That is a hexagon")
elif s == 7:
    print("That is a heptagon")
elif s == 8:
    print("That is a octagon")
elif s == 9:
    print("That is a nonagon")
elif s == 10:
    print("That is a decagon")
else:
    print("Invalid number of sides")
