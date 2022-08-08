n = int(input())
for i in range(n):
    numeros = list(map(int, input().split()))
    print(sum(numeros) - numeros[0] - (numeros[0] - 1))