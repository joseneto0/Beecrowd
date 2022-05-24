matriz = []
maior_toques = 0

for c in range(8):
    matriz.append([0] * 4)

for e in range(20):
    L, C = map(int, input().split())
    for i in range(8):
        for j in range(4):
            matriz[L][C] += 1
            if matriz[L][C] > maior_toques:
                maior_toques = matriz[L][C]

for z in range(8):
    for k in range(4):
        if matriz[z][k] == maior_toques:
            print(f'{z} {k}')