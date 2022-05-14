X = int(input())
Z = int(input())
contador = 2
X_final = X
somador = 1
while Z <= X:
    Z = int(input())
while X_final <= Z:
    X_final += X + somador
    if X_final <= Z:
        contador += 1
        somador += 1
print(contador)