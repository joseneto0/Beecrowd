T = int(input())
for i in range(T):
    fibo = [0, 1]
    N = int(input())
    if N > 1:
        for c in range(2, N+1):
            fibo.append(fibo[c-2] + fibo[c-1])
        print(f'Fib({N}) = {fibo[N]}')
    else:
        print(f'Fib({N}) = {fibo[N]}')