while True:
    try:
        qtd = 0
        n, alturaMinima, alturaMaxima = map(int, input().split())
        for i in range(n):
            valores = int(input())
            if valores >= alturaMinima and valores <= alturaMaxima:
                qtd += 1
        print(qtd)
    except EOFError:
        break