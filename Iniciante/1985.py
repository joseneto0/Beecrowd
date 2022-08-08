n = int(input())
soma = 0
for i in range(n):
    p, q = map(int, input().split())
    if p == 1001:
        soma += (q * 1.5)
    elif p == 1002:
        soma += (q * 2.5)
    elif p == 1003:
        soma += (q * 3.5)
    elif p == 1004:
        soma += (q * 4.5)
    else:
        soma += (q * 5.5)
print(f"{soma:.2f}")
