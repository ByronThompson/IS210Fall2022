import math

a = 9.8

h = float(input("Height of drop (meters): "))

Vf = math.sqrt(2*a*h)

print(f"The Velocity on impact of an object dropped from {h} meters = {Vf} m/s")