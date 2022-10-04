import math

def finVel(height):
    g = 9.8
    return math.sqrt(2*g*height)

h = float(input("Height of drop (meters): "))

print(f"The Velocity on impact of an object dropped from {h} meters = {finVel(h)} m/s")