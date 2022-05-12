from math import sqrt
val = input().split()
A = float(val[0])
B = float(val[1])
C = float(val[2])
delta = (B**2) - 4 * A * C
if delta < 0:
    print('Impossivel calcular')
elif A == 0:
    print('Impossivel calcular')
else:
    x1 = (-B + sqrt(delta)) / (2 * A)
    x2 = (-B - sqrt(delta)) / (2 * A)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
