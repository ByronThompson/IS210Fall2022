import math

def circArea(radius):
    return math.pi * radius ** 2

def sphVol(radius):
    return (4 / 3) * math.pi * radius ** 3


r = float(input("radius: "))

print(f"The area of a circle of radius {r} = {circArea(r)}")
print(f"The volume of a sphere of radius {r} = {sphVol(r)}")