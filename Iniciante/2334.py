while True:
    n = int(input())
    if n == -1:
        break
    if (n-1 < 0):
        print('0')
    else:
        print(n-1)