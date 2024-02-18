x = 1
while True:
    valores = int(input())
    if valores == 0:
        break
    x = 1
    while x <= valores:
        if x == valores:
            print(f'{x}', end ='\n')
        else:
            print(f'{x}', end=' ')
        x += 1