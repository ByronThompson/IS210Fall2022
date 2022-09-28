interest = 0.04

def calcInterest(amount):
    return amount + (amount * interest)


deposit = float(input("Initial deposit: "))

oneYr = calcInterest(deposit)
twoYr = calcInterest(oneYr)
threeYr = calcInterest(twoYr)

print("Savings after One Year:", format(oneYr, ",.2f"))
print("Savings after Two Years:", format(twoYr, ",.2f"))
print("Savings after Three Years:", format(threeYr, ",.2f"))