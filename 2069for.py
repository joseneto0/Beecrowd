matriz = []
bomba = -1
contador_bombas = 0

for i in range(4):
    matriz.append([0] * 6)

N = int(input())
for i in range(N):
    L, C = map(int, input().split())
    L -= 1
    C -= 1
    matriz[L][C] = bomba

L, C = map(int, input().split())
L -= 1
C -= 1

for i in range(-1, 2):
    for j in range(-1, 2):
        if (L + i >= 0 and L + i <= 3) and (C + j >= 0 and C + j <= 5):
            if matriz[L + i][C + j] == bomba:
                contador_bombas += 1

if matriz[L][C] == bomba:
    print('B')
elif contador_bombas == 0:
    print('X')
elif contador_bombas > 0:
    print(contador_bombas)