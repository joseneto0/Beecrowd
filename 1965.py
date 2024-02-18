lugares = []
contador = 0

for i in range(10):
    lugares.append([0] * 20)

for i in range(100):
    F, P = map(int, input().split())
    if lugares[F][P] == 0:
        contador += 1
        lugares[F][P] = 1
print(contador)