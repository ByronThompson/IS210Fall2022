import math

point1N = float(input("First Point °N: "))
point1W = float(input("First Point °W: "))
point2N = float(input("Second Point °N: "))
point2W = float(input("Second Point °W: "))

distance = 6371.01 * math.acos(math.sin(point1N) * math.sin(point2N)
                               * math.cos(point1W) * math.cos(point2W)
                               * math.cos(point1W - point2W))

print(f"The distance between ({point1N}°N, {point1W}°W) and ({point1N}°N, {point2W}°W) is {distance}KM")