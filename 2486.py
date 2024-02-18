dicio = {'sucodelaranja': 120, 'morangofresco': 85, 'mamao': 85, 'goiabavermelha': 70, 'manga': 56, 'laranja': 50, 'brocolis': 34}
nome = ''
qtnds = []
nomes = []
consumo = 0
while True:
    t = int(input())
    if t == 0:
        break
    for i in range(t):
        valores = list(input().split())
        qtnds.append(int(valores[0]))
        del(valores[0])
        for i in valores:
            nome += i
        nomes.append(nome)
        nome = ''
    for i in range(len(qtnds)):
        consumo += dicio[nomes[i]] * qtnds[i]
    if consumo > 130:
        print(f'Menos {consumo - 130} mg')
    elif consumo < 110:
        print(f'Mais {110 - consumo} mg')
    else:
        print(f"{consumo} mg")
    consumo = 0
    qtnds = []
    nomes = []