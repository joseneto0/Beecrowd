n = int(input())
matriz = []
casasPretas = casasBrancas = 0
for i in range(n):
    matriz.append([0] * n)
for i in range(n):
    for j in range(n):
        if i % 2 == 0 and j % 2 != 0:
            matriz[i][j] = 1
        elif i % 2 != 0 and j % 2 == 0:
            matriz[i][j] = 1
        if matriz[i][j] == 1:
            casasPretas += 1
        else:
            casasBrancas += 1
print(f"{casasBrancas} casas brancas e {casasPretas} casas pretas")