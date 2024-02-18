valor = float(input())
if valor <= 2000:
    print('Isento')
elif valor <= 3000:
    imposto = (valor - 2000) * 8/100 
    print(f'R$ {imposto:.2f}')
elif valor <= 4500:
    imposto = (valor - 3000) * 18/100 + 80 #1000 * 8/100
    print(f'R$ {imposto:.2f}')
else:
    imposto = (valor - 4500) * 28/100 + 270 + 80 # 1500 * 18/100, 1000 * 8/100
    print(f'R$ {imposto:.2f}')