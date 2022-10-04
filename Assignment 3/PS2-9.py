interest = 0.04

deposit = float(input("Initial deposit: "))

oneYr = deposit+(deposit*interest)
twoYr = oneYr+(oneYr*interest)
threeYr = twoYr+(twoYr*interest)

print("Savings after One Year:", format(oneYr, ",.2f"))
print("Savings after Two Years:", format(twoYr, ",.2f"))
print("Savings after Three Years:", format(threeYr, ",.2f"))