peca1 = input() .split(' ')
peca2 = input() .split(' ')
c1 = int(peca1[0])
n1 = int(peca1[1])
v1 = float(peca1[2])
c2 = int(peca2[0])
n2 = int(peca2[1])
v2 = float(peca2[2])
calc = (n1 * v1) + (n2 * v2)
print(f'VALOR A PAGAR: R$ {calc:.2f}')