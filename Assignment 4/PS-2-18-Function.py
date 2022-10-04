import math

def cylVol(radius, height):
    area = math.pi * radius ** 2
    return area * height

r = float(input("radius: "))
h = float(input("height: "))

print(f"The volume of a cylinder of radius {r} and height {h} = {format(cylVol(r, h), ',.1f')}")