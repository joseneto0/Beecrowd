n = int(input())
for i in range(n):
    nome, forca = input().split()
    nome = nome.upper()
    forca = int(forca)
    if nome == "THOR":
        print('Y')
    else:
        print('N')