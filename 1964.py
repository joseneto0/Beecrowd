N = int(input())
idades = []
reverso = []
cont_M = 0
for i in range(N):
    I, M = map(int, input().split())
    idades.append(I)
    if M == 12:
        cont_M += 1
media = sum(idades) / len(idades)
print(cont_M)
for m in range(N):
    if idades[m] > media:
        reverso.append(idades[m])
reverso.reverse()
for r in reverso:
    print(r)