while True:
    N = int(input())
    if N == 0:
        break
    dict = {}
    for i in range(N):
        time, pontos = input().split()
        pontos = int(pontos)
        dict[time] = pontos
    for i in range(N//2):
        timeA, gols, timeB = input().split()
        golA, golB = gols.split('-')
        golA, golB = int(golA), int(golB)
        dict[timeA] += (golA * 3)
        dict[timeB] += (golB * 3)
        if golA > golB:
            dict[timeA] += 5
        elif golA < golB:
            dict[timeB] += 5
        else:
            dict[timeA] += 1
            dict[timeB] += 1
    maior = 0
    vencedor = ''
    for i, j in dict.items():
        if j > maior:
            maior = j
            vencedor = i
    if vencedor == 'Sport':
        print(f'O Sport foi o campeao com {maior} pontos :D')
    else:
        print(f'O Sport nao foi o campeao. O time campeao foi o {vencedor} com {maior} pontos :(')
    print()
    dict.clear()