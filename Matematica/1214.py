c = int(input())
rep = 0
while rep < c:
    valores = list(map(int, input().split()))
    cont = 0
    qtd = valores[0]
    valores.pop(0)
    media = sum(valores) / qtd
    for i in valores:
        if i > media:
            cont += 1
    print(f"{cont * 100 / qtd:.3f}%")
    rep += 1