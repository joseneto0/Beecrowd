n = int(input())
for i in range(n):
    nome = input()
    grau = float(input())
    notas = list(map(float, input().split()))
    n = (sum(notas) - max(notas) - min(notas)) * grau
    print(f"{nome} {n:.2f}")