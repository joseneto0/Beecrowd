while True:
    soma = 0
    s = input()
    if s == '*':
        break
    dict = {}   
    lista = []
    valor = 1
    for i in ['W', 'H', 'Q', 'E', 'S', 'T', 'X']:
        dict[i] = valor
        valor /= 2
    for i in range(len(s)):
        if s[i] in dict.keys():
            soma += dict[s[i]]
        else:
            lista.append(soma)
            soma = 0
    contador = len(lista) - 1
    for i in range(len(lista)):
        if lista[i] != 0 and lista[i] != 1:
            contador -= 1
    print(contador)