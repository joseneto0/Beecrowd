n = int(input())
opcoes = ['PROXYCITY', 'P.Y.N.G.', 'DNSUEY!', 'SERVERS', 'HOST!', 'CRIPTONIZE', 'OFFLINE DAY', 'SALT', 'ANSWER!', 'RAR?', 'WIFI ANTENNAS']
for i in range(n):
    n, m = map(int, input().split())
    indice = n + m
    print(opcoes[indice])