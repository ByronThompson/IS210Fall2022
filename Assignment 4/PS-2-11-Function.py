def toLPKM(mpg):
    lp100km = 235.215
    return lp100km/mpg

mpg = float(input("MPG: "))
print(f"{mpg} MPG = {toLPKM(mpg)} L/100KM")
