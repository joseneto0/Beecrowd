Q = int(input())
sucos = []
contador = 0
for i in range(Q):
    suco = int(input())
    sucos.append(suco)
media = sum(sucos) / len(sucos)
litro = sum(sucos) // 1000
for m in range(len(sucos)):
    if sucos[m] < media:
        contador += 1

print(sum(sucos))
print(litro)
print(contador)