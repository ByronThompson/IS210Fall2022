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

def dateToDayNum(month, day):
    d = 0
    if month == "january":
        d = day
    elif month == "february":
        d = 31 + day
    elif month == "march":
        d = 59 + day
    elif month == "april":
        d = (31*2)+28 + day
    elif month == "may":
        d = (31*2)+30+28 + day
    elif month == "june":
        d = (31*3)+30+28 + day
    elif month == "july":
        d = (31*3)+(30*2)+28 + day
    elif month == "august":
        d = (31*4)+(30*2)+28 + day
    elif month == "september":
        d = (31*5)+(30*2)+28 + day
    elif month == "october":
        d = (31 * 5) + (30 * 3) + 28 + day
    elif month == "november":
        d = (31 * 6) + (30 * 3) + 28 + day
    elif month == "december":
        d = (31 * 6) + (30 * 4) + 28 + day

    return d

m = getInputAlpha("Please enter a month: ")
d = getInputNum("Please enter a day: ")

dd = dateToDayNum(m.lower(), d)
s = ""
if dd < 79:
    s = "winter"
elif dd < 172:
    s = "spring"
elif dd < 264:
    s = "summer"
elif dd < 354:
    s = "fall"
else:
    s = "winter"

print(f"{m} {d} is in {s}")