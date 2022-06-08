lista = [0, 0, 0, 0, 0]
st = 'AEIOU'
for i in range(10):
    frase = input().upper()
    for j in range(len(frase)):
        if frase[j] == 'A':
            lista[0] += 1
        if frase[j] == 'E':
            lista[1] += 1
        if frase[j] == 'I':
            lista[2] += 1
        if frase[j] == 'O':
            lista[3] += 1
        if frase[j] == 'U':
            lista[4] += 1
print(st[lista.index(max(lista))])