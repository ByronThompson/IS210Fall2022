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
        return a
    else:
        print("Invalid input")
        return getInputNum(message)