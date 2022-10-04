def daysHourMinuteSecondsToSeconds(d, h, m, s):
    total = days * 24
    total = (total + hours) * 60
    total = (total + minutes) * 60
    total += second
    return total

days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
second = int(input("Seconds: "))

print(f"{days} Days, {hours} Hours, {minutes} Minutes, and {second} Seconds = {daysHourMinuteSecondsToSeconds(days, hours, minutes, second)} Seconds")