# Numeric get input
def getInputNum(message):
    a = input(message)
    if a.isnumeric():
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)

i = getInputNum("Please enter an age in human years: ")

d = i

r = 0

if d >= 2:
    r = (d-2)*4
    d = d-(d-2)

r += abs(d)*10.5

print(f"{i} in human years is {r} in dog years")