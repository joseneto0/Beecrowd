X, Y = map(int, input().split())
numeros = []
for i in range(1, Y + 1):
    numeros.append(i)
    if X == len(numeros):
        print(' '.join(map(str, numeros)))
        numeros = []
    