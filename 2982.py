n = int(input())
somaG = somaV = 0
for i in range(n):
    t, c = input().split()
    c = int(c)
    if t == 'G':
        somaG += c
    else:
        somaV += c
if somaV < somaG:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
else:
    print('A greve vai parar.')