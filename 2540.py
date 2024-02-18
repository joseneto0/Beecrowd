while True:
    try:
        n = int(input())
        valores = list(map(int, input().split()))
        if valores.count(1) >= (2/3) * len(valores):
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break