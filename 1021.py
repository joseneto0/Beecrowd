N, M = input().split('.')
N = int(N)
M = int(M)

nota100 = N // 100
r = N % 100

nota50 = r // 50
r = r % 50

nota20 = r// 20
r = r % 20

nota10 = r // 10
r = r % 10

nota5 = r // 5
r = r % 5

nota2 = r // 2
r = r % 2

moeda1 = r

moeda05 = M // 50
r = M % 50

moeda025 = r // 25
r = r % 25

moeda010 = r // 10
r = r % 10

moeda005 = r // 5
r = r % 5

moeda001 = r

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(nota100))
print('{} nota(s) de R$ 50.00'.format(nota50))
print('{} nota(s) de R$ 20.00'.format(nota20))
print('{} nota(s) de R$ 10.00'.format(nota10))
print('{} nota(s) de R$ 5.00'.format(nota5))
print('{} nota(s) de R$ 2.00'.format(nota2))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(moeda1))
print('{} moeda(s) de R$ 0.50'.format(moeda05))
print('{} moeda(s) de R$ 0.25'.format(moeda025))
print('{} moeda(s) de R$ 0.10'.format(moeda010))
print('{} moeda(s) de R$ 0.05'.format(moeda005))
print('{} moeda(s) de R$ 0.01'.format(moeda001))