n = int(input())
for i in range(n):
    f1, f2 = map(int, input().split())
    restoDivisao = 1
    while restoDivisao != 0:
        restoDivisao = f1 % f2
        f1 = f2
        f2 = restoDivisao
    print(f1)