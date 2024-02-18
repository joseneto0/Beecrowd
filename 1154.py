soma = 0
qntd_idades = 0
while True:
    idades = int(input())
    if idades < 0:
        break
    else:
        soma += idades
        qntd_idades += 1
media = soma / qntd_idades
print(f'{media:.2f}')