N = int(input())
for i in range(1, N+1):
    X = int(input())
    divisoes = 0
    for j in range(1, X+1):
        if X % j == 0:
            divisoes += 1
    if divisoes > 2:
        print(f'{X} nao eh primo')
    else:
        print(f'{X} eh primo')