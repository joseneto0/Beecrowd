salario = float(input())
if salario >= 0 and salario <= 400.00:
    rj15 = salario * 15/100
    print('Novo salario: {:.2f}'.format(salario + rj15))
    print('Reajuste ganho: {:.2f}'.format(rj15))
    print('Em percentual: 15 %')
elif salario > 400.00 and salario <= 800.00:
    rj12 = salario * 12/100
    print('Novo salario: {:.2f}'.format(salario + rj12))
    print('Reajuste ganho: {:.2f}'.format(rj12))
    print('Em percentual: 12 %')
elif salario > 800.00 and salario <= 1200.00:
    rj10 = salario * 10/100
    print('Novo salario: {:.2f}'.format(salario + rj10))
    print('Reajuste ganho: {:.2f}'.format(rj10))
    print('Em percentual: 10 %')
elif salario > 1200.00 and salario <= 2000.00:
    rj7 = salario * 7/100
    print('Novo salario: {:.2f}'.format(salario + rj7))
    print('Reajuste ganho: {:.2f}'.format(rj7))
    print('Em percentual: 7 %')
else:
    rj4 = salario * 4/100
    print('Novo salario: {:.2f}'.format(salario + rj4))
    print('Reajuste ganho: {:.2f}'.format(rj4))
    print('Em percentual: 4 %')