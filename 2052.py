valores = []
while True:
    N = int(input())
    if N not in valores:
        valores.append(N)
    else:
        break
for i in range(len(valores)):
    print(f'{valores[i]}')