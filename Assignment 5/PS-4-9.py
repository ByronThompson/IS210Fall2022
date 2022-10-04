def alphabetic(input):
    if str(input).isalpha():
        return f"{input} is alphabetical"
    elif str(input).isnumeric():
        return f"{input} is a number"
    else:
        return f"{input} is a special character"


print(alphabetic("a"))
