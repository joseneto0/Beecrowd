matriz = []

soma = 0
contador_media = 0
inicio = 11

O = input()
for i in range(12):
    matriz.append([0] * 12)

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

for i in range(1, 11):
    for j in range(inicio, 12):
        soma += matriz[i][j]
        contador_media += 1
    if i < 5:
        inicio -= 1
    elif i > 5:
        inicio += 1

if O == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / contador_media:.1f}')