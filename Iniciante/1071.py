valor_1 = int(input())
valor_2 = int(input())
soma_impares = 0
for i in range(valor_1 - 1, valor_2, -1):
    if i % 2 != 0:
        soma_impares += i
print(soma_impares)