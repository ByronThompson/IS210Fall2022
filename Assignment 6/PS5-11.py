def isMonth(m):
    return m == "january" or m == "february" or m == "march" or m == "april" or m == "may" or m == "june" or m == "july" or m == "august" or m == "september" or m == "october" or m == "november" or m == "december"

# Alphabetic get input
def getInputAlpha(message):
    a = input(message)
    if a.isalpha() and isMonth(a.lower()):
        return a
    else:
        print("Invalid input")
        return getInputAlpha(message)

# Numeric get input
def getInputNum(message):
    a = input(message)
    if a.isnumeric() and (0 < int(a) < 32):
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)


m = getInputAlpha("Please enter a month: ")
d = getInputNum("Please enter a day: ")

if m.lower() == "january" and d == 1:
    print("January 1st is New Year's")
elif m.lower() == "july" and d == 1:
    print("July 1st is Canada Day")
elif m.lower() == "december" and d == 25:
    print("December 25th is Christmas")
else:
    print("The date entered is not a holiday")