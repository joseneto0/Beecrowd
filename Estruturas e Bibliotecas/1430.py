while True:
    soma = 0
    s = input()
    if s == '*':
        break
    dict = {}   
    lista = []
    dict['W'] = 1
    dict['H'] = 0.5
    dict['Q'] = 0.25
    dict['E'] = 0.125
    dict['S'] = 0.0625
    dict['T'] = 0.03125
    dict['X'] = 0.015625
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
        