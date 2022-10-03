def alphabetic(input):
    upper = str(input).upper()
    if str(input) == upper:
        return f"{input} is Upper Case"
    else:
        return f"{input} is lower case"


print(alphabetic("a"))
