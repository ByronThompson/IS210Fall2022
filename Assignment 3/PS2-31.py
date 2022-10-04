i = int(input("Enter a four digit integer: "))

th = i//1000
i = i%1000

h = i//100
i = i%100

t = i//10
i = i%10

final = th+h+t+i

print(f"{th} + {h} + {t} + {i} = {final}")