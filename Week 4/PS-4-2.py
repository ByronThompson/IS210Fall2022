def findMax(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


firstNum = 90
secondNum = 80
thirdNum = 100

print(findMax(firstNum, secondNum, thirdNum))
