n = int(input())
qtdF = qtdM = 0
for i in range(n):
    nome, brinquedo = input().split()
    if brinquedo == 'F':
        qtdF += 1
    else:
        qtdM += 1
print(f"{qtdM} carrinhos")
print(f"{qtdF} bonecas")