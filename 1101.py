while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    menor = min(m, n)
    maior = max(m, n)
    soma = 0
    for i in range(menor, maior+1):
        print(i, end=' ')
        soma += i
    print(f'Sum={soma}')
    
