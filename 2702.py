a = list(map(int, input().split()))
b = list(map(int, input().split()))
qtd = 0
for i in range(3):
    if a[i] < b[i]:
        qtd += b[i] - a[i]
print(qtd)