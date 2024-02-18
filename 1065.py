cont = 0
for i in range(5):
    valores = int(input())
    if valores % 2 == 0:
        cont += 1
print('{} valores pares'.format(cont))