import string
alfabeto = string.ascii_lowercase
n = int(input())
i = 0
while i < n:
    nova_frase = ''
    frase = input()
    for j in range(len(frase)):
        if frase[j].isalpha():
            nova_frase += frase[j]
    if len(set(nova_frase)) == len(alfabeto):
        print('frase completa')
    elif len(set(nova_frase)) >= len(alfabeto) / 2:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
    i += 1