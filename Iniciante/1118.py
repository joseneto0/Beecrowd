novo = 1
nota_valida = 0
media = 0
while novo == 1:
    while nota_valida != 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print('nota invalida')
        else:
            media += nota / 2
            nota_valida += 1
    novo = int(input('novo calculo (1-sim 2-nao)'))
print('media = {:.2f}'.format(media)) 