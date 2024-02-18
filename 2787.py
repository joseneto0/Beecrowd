n = int(input())
m = int(input())
matriz = [] 
for i in range(n):
    matriz.append([0] * m)
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            if j % 2 == 0:
                matriz[i][j] = 1
        else:
            if j % 2 != 0:
                matriz[i][j] = 1
print(matriz[n-1][m-1])