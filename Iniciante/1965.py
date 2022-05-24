lugares = [[0] * 20,[0] * 20,[0] * 20,[0] * 20,[0] * 20,[0] * 20,[0] * 20,[0] * 20,[0] * 20,[0] * 20]
contador = 0

for i in range(10):
    for j in range(10):
        F, P = map(int, input().split())
        if lugares[F][P] == 0:
            contador += 1
            lugares[F][P] = 1
print(contador)