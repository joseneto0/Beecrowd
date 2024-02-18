qtdCaw = 0
numero = 0
while qtdCaw != 3:
    linha = input()
    linha = linha.replace(' ', '')
    if linha.isalpha() == False:
        if linha[0] == '*':
            numero += 4
        if linha[1] == '*':
            numero += 2
        if linha[2] == '*':
            numero += 1
    else:
        qtdCaw += 1
        print(numero)
        numero = 0