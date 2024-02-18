lista = list(map(int, input().split()))
soma = 0
A = 0
N = 0
for i in lista:
    if A == 0:
        A = i
    else:
        if i > 0:
            N = i
            break
for c in range(N):
    soma += A
    A += 1
print(f'{soma}')