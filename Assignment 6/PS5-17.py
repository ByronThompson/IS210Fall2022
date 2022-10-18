import math

def isFloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

# Numeric get input
def getInputNum(message):
    a = input(message)
    if isFloat(a):
        return float(a)
    else:
        print("Invalid input")
        return getInputNum(message)

def calculateRoots(a, b, c):
    dis = (b**2) - (4*a*c)
    if dis < 0:
        print("The function has no root")
        return

    if dis == 0:
        rt = -b/(2*a)
        print(f"The root of the function is {rt}")
        return

    rt1 = (-b + math.sqrt(dis)) / (2 * a)
    rt2 = (-b - math.sqrt(dis)) / (2 * a)
    print(f"The roots of the function are {rt1} and {rt2}")


a = getInputNum("Enter the A value of the quadratic function: ")
b = getInputNum("Enter the B value of the quadratic function: ")
c = getInputNum("Enter the C value of the quadratic function: ")

calculateRoots(a,b,c)
