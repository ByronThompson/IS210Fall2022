# Numeric get input
def getInputNum(message):
    a = input(message)
    if a.isnumeric():
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)

i = getInputNum("Please enter a number: ")

if i%2 == 0:
    print(f"{i} is even")
else:
    print(f"{i} is odd")