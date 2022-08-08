while True:
    n = int(input())
    if n == 0:
        break
    soma = 0
    for i in range(n):
        valores = int(input())
        if (valores - 1) % 2 == 0:
            soma = (valores - 1) * 2 + 1
        else:
            soma = (valores - 2) * 2 + 2
        print(soma)