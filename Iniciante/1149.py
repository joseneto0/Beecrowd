while True:
    A, N = map(int, input().split())
    if N < 0 or N == 0:
        N = True
    A += 1
    N += 1
    print(A + N)
    break