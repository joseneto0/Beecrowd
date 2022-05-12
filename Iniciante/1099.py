num = int(input())
cont = 0
for i in range(1, num + 1):
    x, y = map(int, input().split())
    soma = 0
    if x > y:
        for cont in range(y + 1, x):
            if cont % 2 != 0:
                soma += cont
    if y > x:
        for cont in range(x + 1, y):
            if cont % 2 != 0:
                soma += cont
    if x == y:
        soma = 0
    print(soma)
