n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
if max(lista) == lista[0]:
    print('S')
else:
    print("N")