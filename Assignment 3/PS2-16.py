import math

r = float(input("radius: "))

area = math.pi * r**2
volume = (4/3) * math.pi * r**3

print(f"The area of a circle of radius {r} = {area}")
print(f"The volume of a sphere of radius {r} = {volume}")