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


def monthNumDays(month):
    s = ""
    if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
        s = "31 days"
    elif month == "february":
        s = "28 days in a common year, and 29 days in a leap year"
    else:
        s = "30 days"

    print(f"{month} has {s}")


m = getInputAlpha("Please enter a month: ")
monthNumDays(m)
