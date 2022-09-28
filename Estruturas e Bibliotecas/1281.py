N = int(input())
dicio = {}
for i in range(N):
    cont = 0
    M = int(input())
    for j in range(M):
        s, v = input().split()
        v = float(v)
        dicio[s] = v
    P = int(input())
    for j in range(P):
        s, v = input().split()
        v = int(v)
        if s in dicio.keys():
            cont += (dicio[s] * v)
    print(f"R$ {cont:.2f}")