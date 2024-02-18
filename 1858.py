n = int(input())
numeros = list(map(int, input().split()))
print(numeros.index(min(numeros)) + 1)