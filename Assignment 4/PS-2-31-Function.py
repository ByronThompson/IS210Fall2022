def sumDigits(input):
    th = input // 1000
    toll = input % 1000

    h = toll // 100
    toll = toll % 100

    t = toll // 10
    toll = toll % 10

    return th + h + t + toll

i = int(input("Enter a four digit integer: "))

print(f"The sum of the digits of {i} = {sumDigits(i)}")