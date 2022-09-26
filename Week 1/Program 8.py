excessMinutes = int(input("Please enter the number of excess minutes: "))

overageFee =\
    excessMinutes \
    * 0.35

# The \ character is only needed when breaking expressions, not functions
print("your current overage fee is $",
      format(overageFee, ",.2f"),
      sep="")

print("your current overage fee is $",
      '{0:,.2f}'.format(overageFee),
      sep="")
