valores = []
qntd_notas = 0
while True:
    notas = float(input())
    if notas < 0 or notas > 10:
        print('nota invalida')
    else:
        valores.append(notas)
        qntd_notas += 1
        if qntd_notas == 2:
            break
media = sum(valores) / 2
print(f'media = {media:.2f}')