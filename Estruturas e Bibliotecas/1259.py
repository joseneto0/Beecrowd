n = int(input())
pares = []
impares = []
for i in range(n):
    v = int(input())
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
pares.sort()
impares.sort(reverse=True)
for i in range(len(pares)):
    print(pares[i])
for i in range(len(impares)):
    print(impares[i])