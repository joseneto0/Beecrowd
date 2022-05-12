valor = int(input())
if valor % 2 != 0:
    valor += 1
for i in range(2, valor + 1, 2):
    print('{}^2 = {}'.format(i, i ** 2))