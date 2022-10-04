import math

r = float(input("radius: "))
h = float(input("height: "))

area = math.pi * r**2
volume = area*h

print(f"The volume of a cylinder of radius {r} and height {h} = {format(volume, ',.1f')}")