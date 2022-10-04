smallRefund = 0.10
largeRefund = 0.25

s = int(input("Number of small bottles (1 liter or less): "))
l = int(input("Number of large bottles (more than 1 liter): "))

r = (s*smallRefund)+(l*largeRefund)

print("Your refund will be $", format(r, ",.2f"), sep="")