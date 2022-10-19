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

def withinOneHz(freq, test):
    return test-1 < freq < test+1

f = getInputNum("Please enter a frequency")
s = ""

if withinOneHz(f, 261.63):
    s = "C4"
elif withinOneHz(f, 293.66):
    s = "D4"
elif withinOneHz(f, 329.63):
    s = "E4"
elif withinOneHz(f, 349.23):
    s = "F4"
elif withinOneHz(f, 392.00):
    s = "G4"
elif withinOneHz(f, 440.00):
    s = "A4"
elif withinOneHz(f, 493.88):
    s = "B4"

if s == "":
    print("That is not a known frequency")
else:
    print(f"A frequency of {f}hz corresponds to a {s}")