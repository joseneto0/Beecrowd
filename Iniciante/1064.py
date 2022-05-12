cont = 0
soma_positivos = 0
for c in range(6):
    v = float(input())
    if v > 0:
        cont += 1
        soma_positivos += v
        media = soma_positivos / cont
print('{} valores positivos'.format(cont))
print('{:.1f}'.format(media))