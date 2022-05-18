N = int(input())
for i in range(N):
    soma = 0
    impares = 1
    X, Y = map(int, input().split())
    while impares <= Y:
        if X % 2 != 0:
            soma += X
            X += 1
            impares += 1
        else:
            X += 1
    print(soma)