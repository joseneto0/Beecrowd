count_max = 0
nome = input().upper()
while nome != 'FIM':
    nomes = []
    for i in nome:
        if i not in nomes:
            if i >= 'A' and i <= 'Z':
                nomes.append(i)
    if len(nomes) > 10:
        count_max += 1
    nome = input().upper()
print(count_max)
#apelei por listas msm, n consegui via str :/