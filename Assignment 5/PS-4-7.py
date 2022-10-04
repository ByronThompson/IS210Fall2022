def alphabetic(input):
    if str(input).isalpha():
        return f"{input} is alphabetical"
    else:
        return f"{input} is not alphabetical"


print(alphabetic("A"))
