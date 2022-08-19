M, N = map(int, input().split())
dict = {}
rep = 0
somador = 0
for i in range(M):
    nome, valor = input().split()
    valor = int(valor)
    dict[nome] = valor
while rep < N:
    texto = input()
    if texto == '.':
        print(somador)
        rep += 1
        somador = 0
    else:
        for i in dict.keys():
            somador += texto.count(i) * dict[i]