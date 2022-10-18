import string

# Alphabetic get input
def getInputAlpha(message):
    a = input(message)
    if a.isalpha():
        return a
    else:
        print("Invalid input")
        return getInputAlpha(message)

# Numeric get input
def getInputNum(message):
    a = input(message)
    if a.isnumeric():
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)

c = getInputAlpha("Please enter a board column: ")
r = getInputNum("Please enter a board row: ")

i = string.ascii_lowercase.index(c)
i = ((i+1)%2)

if (r+i)%2 == 0:
    print(f"{c}{r} is a black space")
else:
    print(f"{c}{r} is a white space")