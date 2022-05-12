num = input().split()
A = int(num[0])
B = int(num[1])
C = int(num[2])
D = int(num[3])
if B > C and D > A and C + D > A + B and C and D > 0 and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
