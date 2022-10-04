def calcRefund(small, large):
    smallRefund = 0.10
    largeRefund = 0.25

    return (small * smallRefund) + (large * largeRefund)


s = int(input("Number of small bottles (1 liter or less): "))
l = int(input("Number of large bottles (more than 1 liter): "))

print("Your refund will be $", format(calcRefund(s, l), ",.2f"), sep="")