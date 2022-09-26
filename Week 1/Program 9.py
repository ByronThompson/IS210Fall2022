originalPrice = float(input("Enter the item's original price: "))
sale = float(input("Please enter the sale amount (ex. %20): %"))

discount = originalPrice * (sale/100)

salePrice = originalPrice - discount

print("The price with the sale is $", format(salePrice, ",.2f"), sep="")
