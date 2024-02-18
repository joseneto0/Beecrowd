n, g = map(int, input().split())
dicio = {}
soma = 0
for i in range(n):
    Ri, Vi = input().split()
    Vi = int(Vi)
    dicio[Ri] = Vi
qtdRunas = int(input())
runasRecitadas = input().split()
for i in range(qtdRunas):
    if runasRecitadas[i] in dicio:
        soma += dicio[runasRecitadas[i]]
    else:
        soma += 0
print(soma)
if soma >= g:
    print('You shall pass!')
else:
    print('My precioooous')