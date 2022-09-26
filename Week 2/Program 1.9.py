COVER_PRICE = 24.95
DISCOUNT = 0.40
SHIPPING_FIRST = 3
SHIPPING_ADDITIONAL = 0.75

copies = int(input("How many copies are you purchasing? "))

subtotal = COVER_PRICE*copies
discount = (COVER_PRICE*copies)*DISCOUNT
shipping = (SHIPPING_FIRST + (SHIPPING_ADDITIONAL * (copies-1)))
total = (subtotal-discount)+shipping

print("Subtotal:", format(subtotal, ",.2f"))
print("Discount:", format(discount, ",.2f"))
print("Shipping:", format(shipping, ",.2f"))
print("-"*25)
print("Total:", format(total, ",.2f"))