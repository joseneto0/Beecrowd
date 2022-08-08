n = int(input())
total_s = acertos_s = total_b = acertos_b = total_a = acertos_a = 0
for i in range(n):
    nome = input()
    s, b, a = map(int, input().split())
    s1, b1, a1 = map(int, input().split())
    total_s += s
    total_b += b
    total_a += a
    acertos_s += s1
    acertos_b += b1
    acertos_a += a1
print(f"Pontos de Saque: {acertos_s * 100 / total_s:.2f} %.")
print(f"Pontos de Bloqueio: {acertos_b * 100 / total_b:.2f} %.")
print(f"Pontos de Ataque: {acertos_a * 100 / total_a:.2f} %.")