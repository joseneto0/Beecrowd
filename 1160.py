T = int(input())
for i in range(T):
    pa, pb, g1, g2 = input().split()
    pa, pb = int(pa), int(pb)
    g1, g2 = float(g1), float(g2)
    contador = 0
    while pa <= pb:
        conta_pa = int(pa * (g1/100))
        pa += conta_pa
        conta_pb = int(pb * (g2/100))
        pb += conta_pb
        contador += 1
        if contador > 100:
            print('Mais de 1 seculo.')
            break
    if contador <= 100:
        print(f'{contador} anos.')