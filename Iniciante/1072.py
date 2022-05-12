valor_inicial = int(input())
contador_in = 0
contador_out = 0
for i in range(valor_inicial):
    valores = int(input())
    if valores >= 10 and valores <= 20:
        contador_in += 1
    else:
        contador_out += 1
print('{} in'.format(contador_in))
print('{} out'.format(contador_out))