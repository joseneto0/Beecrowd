n = int(input())
for i in range(n):
    s = ''
    a, b = input().split()
    if a[len(a) - len(b):] == b:
        print('encaixa')
    else:
        print('nao encaixa')