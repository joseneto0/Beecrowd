N = int(input())
for i in range(0, N):
    numeros = int(input())
    soma = 0
    qntd = 1
    while qntd < numeros:
        if numeros % qntd == 0:
            soma += qntd
        qntd += 1
    if soma == numeros:
        print(f'{numeros} eh perfeito')
    else:
        print(f'{numeros} nao eh perfeito')