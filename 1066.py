contador_par = 0
contador_impar = 0
valores_positivos = 0
valores_negativos = 0
for i in range(5):
    valores = int(input())
    if valores % 2 == 0:
        contador_par += 1
    if valores % 2 != 0:
        contador_impar += 1
    if valores > 0:
        valores_positivos += 1
    if valores < 0:
        valores_negativos += 1
print('{} valor(es) par(es)'.format(contador_par))
print('{} valor(es) impar(es)'.format(contador_impar))
print('{} valor(es) positivo(s)'.format(valores_positivos))
print('{} valor(es) negativo(s)'.format(valores_negativos))