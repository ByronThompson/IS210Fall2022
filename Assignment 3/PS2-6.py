taxRate = 0.09
tipRate = 0.18

sub = float(input("Subtotal: "))

tax = taxRate*sub
tip = tipRate*sub
total = sub + tax + tip

print("Tax:", format(tax, ",.2f"))
print("Tip:", format(tip, ",.2f"))
print("-"*10)
print("Total:", format(total, ",.2f"))
