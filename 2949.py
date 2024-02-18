n = int(input())
qtdHobbit = qtdHumano = qtdElfo = qtdAnao = qtdMago = 0
for i in range(n):
    nome, tipo = input().split()
    if tipo == "X":
        qtdHobbit += 1
    elif tipo == "A":
        qtdAnao += 1
    elif tipo == "E":
        qtdElfo += 1
    elif tipo == "H":
        qtdHumano += 1
    elif tipo == "M":
        qtdMago += 1
print(f"{qtdHobbit} Hobbit(s)")
print(f"{qtdHumano} Humano(s)")
print(f"{qtdElfo} Elfo(s)")
print(f"{qtdAnao} Anao(oes)")
print(f"{qtdMago} Mago(s)")