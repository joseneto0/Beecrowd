N = []
valor = float(input())
for i in range(100):
    N.append(valor)
    print(f'N[{i}] = {valor:.4f}')
    valor /= 2