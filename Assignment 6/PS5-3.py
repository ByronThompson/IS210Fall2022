# Alphabetic get input
def getInputAlpha(message):
    a = input(message)
    if a.isalpha():
        return a
    else:
        print("Invalid input")
        return getInputAlpha(message)

l = getInputAlpha("Please enter a letter: ")

l = l.lower()

if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
    print(f"{l} is a vowel")
elif l == "y":
    print(f"{l} is sometimes a vowel, and sometimes a consonant")
else:
    print(f"{l} is a consonant")