while True:
    valor = int(input())
    soma = 0
    pares = 1
    if valor == 0:
        break
    else:
        while pares <= 5:
            if valor % 2 == 0:
                soma += valor
                valor += 1
                pares += 1
            else:
                valor += 1
        print(soma)