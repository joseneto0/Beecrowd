O = input()
matriz = []

for z in range(12):
    matriz.append([])
    for v in range(12):
        valores = float(input())
        matriz[z].append(valores)


if O == 'S':
    soma = 0
    contador = 1 
    for c in range(11):
        for l in range(contador, 12):
            soma += matriz[c][l]
        contador += 1
    print(f'{soma:.1f}')

if O == 'M':
    soma = 0
    contador = 1
    contador_media = 0
    for c in range(11):
        for l in range(contador, 12):
            soma += matriz[c][l]
            contador_media += 1
        contador += 1
    media = soma / contador_media
    print(f'{media:.1f}')