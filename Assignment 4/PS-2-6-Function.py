taxRate = 0.09
tipRate = 0.18


def printTaxesAndTotal(subTotal):
    tax = taxRate*subTotal
    tip = tipRate*subTotal
    total = subTotal + tax + tip

    print("Tax:", format(tax, ",.2f"))
    print("Tip:", format(tip, ",.2f"))
    print("-"*10)
    print("Total:", format(total, ",.2f"))


sub = float(input("Subtotal: "))
printTaxesAndTotal(sub)
