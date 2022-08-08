n = int(input())
ultimo=1
penultimo=1
if n == 1:
    print(1)
else:
    lista = [1 , 1]
    count= 3
    while count <= n:
        termo = ultimo + penultimo
        lista.append(termo)
        penultimo = ultimo
        ultimo = termo
        count += 1
    lista.reverse()
    print(*lista)