# Numeric get input
def getInputNum(message):
    a = input(message)
    if a.isnumeric():
        return int(a)
    else:
        print("Invalid input")
        return getInputNum(message)

d = getInputNum("Please enter a denomination of US Dollars: ")

if d == 1:
    print("George Washington is on the $1 bill")
elif d == 2:
    print("Thomas Jefferson is on the $2 bill")
elif d == 5:
    print("Abraham Lincoln is on the $5 bill")
elif d == 10:
    print("Alexander Hamilton is on the $10 bill")
elif d == 20:
    print("Andrew Jackson is on the $20 bill")
elif d == 50:
    print("Ulysses S. Grant is on the $50 bill")
elif d == 100:
    print("Benjamin Franklin  is on the $100 bill")
else:
    print(f"{d} is not a denomination of US Dollar")