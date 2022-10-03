def divisibleBy5and11(input):
    if input%5 == 0 and input%11 == 0:
        return f"{input} is divisible by 5 and 11"
    else:
        return f"{input} is not divisible by 5 and 11"


print(divisibleBy5and11(55))
