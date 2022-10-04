import math

def printMath(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"Log10({a}) = {math.log10(a)}")
    print(f"{a}^{b} = {a ** b}")


a = int(input("a = "))
b = int(input("b = "))

printMath(a, b)
