def checkSign(input):
    if input > 0:
        return "Positive"
    elif input < 0:
        return "Negative"
    else:
        return "Zero"


test = 0

print(checkSign(test))
