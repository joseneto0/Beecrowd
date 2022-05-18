pares = []
impares = []
for i in range(15):
    valores = int(input())
    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)
    if len(pares) == 5:
        contador = 0
        for p in pares:
            print(f'par[{contador}] = {p}')
            contador += 1
        pares = []
    if len(impares) == 5:
        contador = 0
        for im in impares:
            print(f'impar[{contador}] = {im}')
            contador += 1
        impares = []

if len(impares) > 0:
    contador = 0
    for c in impares:
        print(f'impar[{contador}] = {c}')
        contador += 1
if len(pares) > 0:
    contador = 0
    for c in pares:
        print(f'par[{contador}] = {c}')
        contador += 1