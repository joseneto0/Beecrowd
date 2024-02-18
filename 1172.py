numeros = []
for i in range(10):
    numeros.append(int(input()))
    if numeros[i] <= 0:
        print(f'X[{i}] = 1')
    else:
        print(f'X[{i}] = {numeros[i]}')