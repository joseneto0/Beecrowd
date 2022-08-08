n = int(input())
for i in range(n):
    a, b = input().split()
    s = ''
    ns = ''
    cont = 0
    for i in range(len(a)-1,-1,-1):
        s += a[i]
        cont += 1
        if cont == len(b):
            break
    for i in range(len(s)-1,-1,-1):
        ns += s[i]
    if ns == b:
        print('encaixa')
    else:
        print('nao encaixa')