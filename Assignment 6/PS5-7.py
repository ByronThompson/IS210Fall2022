# Numeric get input
def getInputNum(message):
    a = input(message)
    if a.isnumeric():
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)


a = getInputNum("Please enter the length of the first side: ")
b = getInputNum("Please enter the length of the second side: ")
c = getInputNum("Please enter the length of the third side: ")

s = ""
if a == b == c:
    s = "equilateral"
elif a == b or a == c or b == c:
    s = "isosceles"
else:
    s = "scalene"

print(f"You have described a {s} triangle")