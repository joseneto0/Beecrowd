while True:
    try:
        x, y, m = map(int, input().split())
        for i in range(m):
            a, b = map(int, input().split())
            if a <= x and b <= y or a <= y and b <= x:
                print('Sim')
            else:
                print('Nao')
    except EOFError:
        break