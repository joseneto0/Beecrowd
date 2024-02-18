matriz = []
soma = 0
media = 0

O = input()
for m in range(12):
    matriz.append([])
    for i in range(12):
        valores = float(input())
        matriz[m].append(valores)

contador = 0
contador_media = 0
for l in range(11, 0, -1):
    contador += 1
    for c in range(contador, 12):
        if O == 'S':
            soma += matriz[c][l]
        if O == 'M':
            soma += matriz[c][l]
            contador_media += 1
            media = soma / contador_media
if O == 'S':
    print(f'{soma:.1f}')
elif O == 'M':
    print(f'{media:.1f}')