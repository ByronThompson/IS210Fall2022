# Numeric get input
def getInputNum(message):
    a = input(message)
    if a.isnumeric():
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)

i = getInputNum("Please enter a number of decibels: ")

s = ""

if i > 130:
    s = "louder than a Jackhammer"
elif i == 130:
    s = "as loud as a Jackhammer"
elif i > 106:
    s = "louder than a lawnmower, but quieter than a jackhammer"
elif i == 106:
    s = "as loud as a lawnmower"
elif i > 70:
    s = "louder than an alarm clock, but quieter than a lawnmower"
elif i == 70:
    s = "as loud as an alarm clock"
elif i > 40:
    s = "louder than a quiet room, but quieter than an alarm clock"
elif i == 40:
    s = "as quiet as a quiet room"
else:
    s = "quieter than a quiet room"

print(f"{i} decibels is {s}")
