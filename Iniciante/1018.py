valor = int(input())

valor1 = valor // 100
r = valor % 100

valor2 = r // 50
r = r % 50

valor3 = r// 20
r = r % 20

valor4 = r // 10
r = r % 10

valor5 = r // 5
r = r % 5

valor6 = r // 2
r = r % 2

valor7 = r // 1
r = r % 1

print(valor)
print(f'{valor1} nota(s) de R$ 100,00')
print(f'{valor2} nota(s) de R$ 50,00')
print(f'{valor3} nota(s) de R$ 20,00')
print(f'{valor4} nota(s) de R$ 10,00')
print(f'{valor5} nota(s) de R$ 5,00')
print(f'{valor6} nota(s) de R$ 2,00')
print(f'{valor7} nota(s) de R$ 1,00')