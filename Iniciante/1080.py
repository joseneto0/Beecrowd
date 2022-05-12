num = int(input())
cont = 0
for i in range(1, 100):
    valores = int(input())
    if valores > cont:
        maior = valores
        posicao = i + 1
        cont = valores
print(maior)
print(posicao)