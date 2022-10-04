futureVal = float(input("Enter the desired future value: "))

rate = float(input("Please enter the annual interest rate: "))

years = int(input("How many years will you allow the future to appreciate: "))

presentValue = futureVal/(1+rate)**years

print("You will need to deposit $", format(presentValue, ",.2f"), sep="")