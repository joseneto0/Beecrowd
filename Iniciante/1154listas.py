idades = []
while True:
    ids = int(input())
    if ids < 0:
        break
    else:
        idades.append(ids)
media = sum(idades) / len(idades)
print(f'{media:.2f}')