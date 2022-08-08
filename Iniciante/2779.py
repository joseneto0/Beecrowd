n = int(input())
m = int(input())
figurinha = []
for i in range(m):
    valores = int(input())
    if valores not in figurinha:
        figurinha.append(valores)
print(abs(n - len(figurinha)))