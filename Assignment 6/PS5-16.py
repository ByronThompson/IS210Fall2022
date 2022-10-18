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

r = getInputNum("Please enter a Richter Scale value: ")

s = ""

if r < 2.0:
    s = "micro"
elif r < 3.0:
    s = "Very Minor"
elif r < 4.0:
    s = "Minor"
elif r < 5.0:
    s = "Light"
elif r < 6.0:
    s = "Moderate"
elif r < 7.0:
    s = "Strong"
elif r < 8.0:
    s = "Major"
elif r < 10.0:
    s = "Great"
else:
    s = "Meteoric"


print(f"A magnitude {r} Earthquake is considered {s}")

