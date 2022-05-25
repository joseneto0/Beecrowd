matriz = []

inicio = 5
fim = 7
soma = 0
contador_media = 0

O = input()

for i in range(12):
    matriz.append([0] * 12)

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

for i in range(7, 12):
    for j in range(inicio, fim):
        soma += matriz[i][j]
        contador_media += 1
    inicio -= 1
    fim += 1

if O == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / contador_media:.1f}')