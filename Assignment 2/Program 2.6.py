TAX_RATE = 0.08

subtotal = float(input("How much was your bill? $"))
tipRate = float(input("What percentage would you like to tip? %"))/100

tax = subtotal*TAX_RATE
tip = subtotal*tipRate

print("subtotal: $", '{0:,.2f}'.format(subtotal), sep="")
print("tax:      $", '{0:,.2f}'.format(tax), sep="")
print("tip:      $", '{0:,.2f}'.format(tip), sep="")
print("-"*20)
print("Total:    $", '{0:,.2f}'.format(subtotal+tax+tip), sep="")
