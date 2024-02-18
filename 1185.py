matriz = []
soma = 0
media = 0

O = input()
for m in range(12):
    matriz.append([])
    for j in range(12):
        valores = float(input())
        matriz[m].append(valores)

contador = 12
contador_media = 0
for l in range(11):
    contador -= 1
    for c in range(0, contador):
        if O == 'S':
            soma += matriz[c][l]
        elif O == 'M':
            soma += matriz[c][l]
            contador_media += 1
            media = soma / contador_media
if O == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{media:.1f}')