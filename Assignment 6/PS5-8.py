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
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)

def calculateFreq(note, octave):
    if note == "c":
        return 261.63/(2**(4-octave))
    elif note == "d":
        return 293.66 / (2 ** (4 - octave))
    elif note == "e":
        return 329.63 / (2 ** (4 - octave))
    elif note == "f":
        return 349.23 / (2 ** (4 - octave))
    elif note == "g":
        return 392.00 / (2 ** (4 - octave))
    elif note == "a":
        return 440.00 / (2 ** (4 - octave))
    elif note == "b":
        return 493.88 / (2 ** (4 - octave))


n = getInputAlpha("Please enter a note: ")
o = getInputNum("Please enter an octave: ")

f = calculateFreq(n.lower(),o)

print(f"A {n}{o} note is {f}hz")
