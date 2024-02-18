matriz = []

for i in range(6):
    matriz.append([' '] * 6)
        
N = int(input())
for j in range(N):
    X, Y = map(int, input().split())
    matriz[X][Y] = '*'

for k in matriz:
    print(k)