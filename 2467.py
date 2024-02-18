N = int(input())
codigo = []
nomes = []
contador = 0
for i in range(N):
    C, nome = input().split()
    C = int(C)
    nome = str(nome)
    codigo.append(C)
    nomes.append(nome)

V = int(input())
votos = [0] * len(codigo)
while V != 0:
    contador += 1
    for v in range(len(codigo)):    
        if V == codigo[v]:
            votos[v] += 1
    V = int(input())

print(contador)
for c in range(len(codigo)):
    print(f'{codigo[c]} {nomes[c]} {votos[c]}')