lista = []
T = int(input())
for i in range(1000):
    l = 0
    while l < T:
        lista.append(l)
        l += 1
    print(f'N[{i}] = {lista[i]}')