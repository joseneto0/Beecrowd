while True:
    try:
        num = int(input())
        c = n = 0 
        for i in range(num):
            v1, v2 = map(int, input().split())
            c += v2
            n += v1 * v2
        conta = n / (c * 100)
        print(f"{conta:.4f}")
    except EOFError:
        break