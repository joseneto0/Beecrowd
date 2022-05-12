m = 1
n = 1
cont = 0
while m <= 0 or n <= 0:
    m, n = map(int, input().split())
    if m > n:
        if n % 2 == 0:
            for i in range(n, m):
                cont += 1
                print('{}'.format(i), end='')
                print('Sum={}'.format(cont), end='')