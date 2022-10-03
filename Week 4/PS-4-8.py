def vowel(input):
    lower = str(input).lower()
    if lower == "a" or lower == "e" or lower == "i" or lower == "o" or lower == "u":
        return f"{input} is a vowel"
    else:
        return f"{input} is a consonant"


print(vowel("o"))
