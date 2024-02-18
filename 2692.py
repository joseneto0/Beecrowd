trocas, palavras = map(int, input().split())
dicio = {}
palavras_final = ''
for i in range(trocas):
    p = input().split()
    dicio[p[0]] = p[1]
    dicio[p[1]] = p[0]
for i in range(palavras):
    palavras_sem_trocar = input()
    for j in range(len(palavras_sem_trocar)):
        if palavras_sem_trocar[j] in dicio:
            palavras_final += dicio[palavras_sem_trocar[j]]
        else:
            palavras_final += palavras_sem_trocar[j]
    print(palavras_final)
    palavras_final =''
