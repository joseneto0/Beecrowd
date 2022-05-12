lista = [0] * 100
for i in range(100):
    lista[i] = float(input())
    if lista[i] <= 10:
        print(f'A[{i}] = {lista[i]}')