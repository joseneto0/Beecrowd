n = int(input())
for i in range(n):
    b = int(input())
    a1, d1, l1 = map(int, input().split())
    a2, d2, l2 = map(int, input().split())
    valorGolpe_dabriel = (a1 + d1) / 2
    if l1 % 2 == 0:
        valorGolpe_dabriel += b
    valorGolpe_guarte = (a2 + d2) / 2
    if l2 % 2 == 0:
        valorGolpe_guarte += b
    if valorGolpe_dabriel > valorGolpe_guarte:
        print('Dabriel')
    elif valorGolpe_dabriel < valorGolpe_guarte:
        print('Guarte')
    elif valorGolpe_guarte == valorGolpe_dabriel:
        print('Empate')