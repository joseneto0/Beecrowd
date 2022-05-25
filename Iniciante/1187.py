matriz = []
O = input()
inicio = 1
fim = 11
soma = 0
contador_media = 0

for i in range(12):
    matriz.append([0] * 12)

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

for i in range(5):
    for j in range(inicio, fim):
        soma += matriz[i][j]
        contador_media += 1
    inicio += 1
    fim -= 1

if O == 'S':
    print(f'{soma:.1f}')

if O == 'M':
    print(f'{soma / contador_media:.1f}')