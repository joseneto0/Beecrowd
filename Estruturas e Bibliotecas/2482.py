N = int(input())
dict = {}
for i in range(N):
    idioma = input()
    natal = input()
    dict[idioma] = natal
M = int(input())
for i in range(M):
    nome = input()
    idioma = input()
    if idioma in dict.keys():
        print(nome)
        print(dict[idioma])
        print()