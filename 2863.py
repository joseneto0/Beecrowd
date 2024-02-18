while True:
    try:
        valores = []
        n = int(input())
        for i in range(n):
            valores.append(float(input()))
        print(min(valores))
    except EOFError:
        break