days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
second = int(input("Seconds: "))

total = days*24
total = (total+hours)*60
total = (total+minutes)*60
total += second

print(f"{days} Days, {hours} Hours, {minutes} Minutes, and {second} Seconds = {total} Seconds")
