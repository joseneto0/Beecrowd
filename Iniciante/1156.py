S = 1
cima = 3
baixo = 2
for i in range(1, 40, 2):
    S += cima/baixo
    cima += 2
    baixo *= 2
print(f'{S:.2f}')