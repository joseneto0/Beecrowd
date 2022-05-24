matriz = []
bomba = -1
contador_bombas = 0

for i in range(4):
    matriz.append([0] * 6)

N = int(input())
for i in range(N):
    L, C = map(int, input().split())
    L -= 1
    C -= 1
    matriz[L][C] = bomba

j1, j2 = map(int, input().split())
j1 -= 1
j2 -= 1

#caso o local onde o jogador escolheu tenha bombas
if matriz[j1][j2] == bomba:
    print('B')

#verificar a quantidade de dicas caso o local não tenha bomba
elif matriz[j1][j2] == 0:

    #Quinas
    if j1 == 0 and j2 == 0:
        if matriz[0][1] == bomba:
            contador_bombas += 1
        if matriz[1][0] == bomba:
            contador_bombas += 1
        if matriz[1][1] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')
    elif j1 == 3 and j2 == 0:
        if matriz[2][0] == bomba:
            contador_bombas += 1
        if matriz[2][1] == bomba:
            contador_bombas += 1
        if matriz[3][1] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')
    elif j1 == 0 and j2 == 5:
        if matriz[0][4] == bomba:
            contador_bombas += 1
        if matriz[1][4] == bomba:
            contador_bombas += 1
        if matriz[1][5] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')
    elif j1 == 3 and j2 == 5:
        if matriz[2][4] == bomba:
            contador_bombas += 1
        if matriz[2][5] == bomba:
            contador_bombas += 1
        if matriz[3][4] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Teto (matriz[0][1])
    elif j1 == 0 and j2 == 1:
        if matriz[0][0] == bomba:
            contador_bombas += 1
        if matriz[1][0] == bomba:
            contador_bombas += 1
        if matriz[1][1] == bomba:
            contador_bombas += 1
        if matriz[1][2] == bomba:
            contador_bombas += 1
        if matriz[0][2] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Teto (matriz[0][2])
    elif j1 == 0 and j2 == 2:
        if matriz[0][1] == bomba:
            contador_bombas += 1
        if matriz[1][1] == bomba:
            contador_bombas += 1
        if matriz[1][2] == bomba:
            contador_bombas += 1
        if matriz[1][3] == bomba:
            contador_bombas += 1
        if matriz[0][3] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Teto(matriz[0][3])
    elif j1 == 0 and j2 == 3:
        if matriz[0][2] == bomba:
            contador_bombas += 1
        if matriz[1][2] == bomba:
            contador_bombas += 1
        if matriz[1][3] == bomba:
            contador_bombas += 1
        if matriz[1][4] == bomba:
            contador_bombas += 1
        if matriz[0][4] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Teto(matriz[0][4])
    elif j1 == 0 and j2 == 4:
        if matriz[0][3] == bomba:
            contador_bombas += 1
        if matriz[1][3] == bomba:
            contador_bombas += 1
        if matriz[1][4] == bomba:
            contador_bombas += 1
        if matriz[1][5] == bomba:
            contador_bombas += 1
        if matriz[0][5] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Chão(matriz[3][1])
    elif j1 == 3 and j2 == 1:
        if matriz[3][0] == bomba:
            contador_bombas += 1
        if matriz[2][0] == bomba:
            contador_bombas += 1
        if matriz[2][1] == bomba:
            contador_bombas += 1
        if matriz[2][2] == bomba:
            contador_bombas += 1
        if matriz[3][2] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Chão(matriz[3][2])
    elif j1 == 3 and j2 == 2:
        if matriz[3][1] == bomba:
            contador_bombas += 1
        if matriz[2][1] == bomba:
            contador_bombas += 1
        if matriz[2][2] == bomba:
            contador_bombas += 1
        if matriz[2][3] == bomba:
            contador_bombas += 1
        if matriz[3][3] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Chão(matriz[3][3])
    elif j1 == 3 and j2 == 3:
        if matriz[3][2] == bomba:
            contador_bombas += 1
        if matriz[2][2] == bomba:
            contador_bombas += 1
        if matriz[2][3] == bomba:
            contador_bombas += 1
        if matriz[2][4] == bomba:
            contador_bombas += 1
        if matriz[3][4] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Chão(matriz[3][4])
    elif j1 == 3 and j2 == 4:
        if matriz[3][3] == bomba:
            contador_bombas += 1
        if matriz[2][3] == bomba:
            contador_bombas += 1
        if matriz[2][4] == bomba:
            contador_bombas += 1
        if matriz[2][5] == bomba:
            contador_bombas += 1
        if matriz[3][5] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Esquerda(matriz[1][0])
    elif j1 == 1 and j2 == 0:
        if matriz[0][0] == bomba:
            contador_bombas += 1
        if matriz[0][1] == bomba:
            contador_bombas += 1
        if matriz[1][1] == bomba:
            contador_bombas += 1
        if matriz[2][1] == bomba:
            contador_bombas += 1
        if matriz[2][0] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Esquerda(matriz[2][0])
    elif j1 == 2 and j2 == 0:
        if matriz[1][0] == bomba:
            contador_bombas += 1
        if matriz[1][1] == bomba:
            contador_bombas += 1
        if matriz[2][1] == bomba:
            contador_bombas += 1
        if matriz[3][1] == bomba:
            contador_bombas += 1
        if matriz[3][0] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Direita(matriz[1][5])
    elif j1 == 1 and j2 == 5:
        if matriz[0][5] == bomba:
            contador_bombas += 1
        if matriz[0][4] == bomba:
            contador_bombas += 1
        if matriz[1][4] == bomba:
            contador_bombas += 1
        if matriz[2][4] == bomba:
            contador_bombas += 1
        if matriz[2][5] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #Direita(matriz[2][5])
    elif j1 == 2 and j2 == 5:
        if matriz[1][5] == bomba:
            contador_bombas += 1
        if matriz[1][4] == bomba:
            contador_bombas += 1
        if matriz[2][4] == bomba:
            contador_bombas += 1
        if matriz[3][4] == bomba:
            contador_bombas += 1
        if matriz[3][5] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #meio(matriz[1][1])
    elif j1 == 1 and j2 == 1:
        if matriz[0][0] == bomba:
            contador_bombas += 1
        if matriz[0][1] == bomba:
            contador_bombas += 1
        if matriz[0][2] == bomba:
            contador_bombas += 1
        if matriz[1][0] == bomba:
            contador_bombas += 1
        if matriz[1][2] == bomba:
            contador_bombas += 1
        if matriz[2][0] == bomba:
            contador_bombas += 1
        if matriz[2][1] == bomba:
            contador_bombas += 1
        if matriz[2][2] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #meio(matriz[1][2])
    elif j1 == 1 and j2 == 2:
        if matriz[0][1] == bomba:
            contador_bombas += 1
        if matriz[0][2] == bomba:
            contador_bombas += 1
        if matriz[0][3] == bomba:
            contador_bombas += 1
        if matriz[1][1] == bomba:
            contador_bombas += 1
        if matriz[1][3] == bomba:
            contador_bombas += 1
        if matriz[2][1] == bomba:
            contador_bombas += 1
        if matriz[2][2] == bomba:
            contador_bombas += 1
        if matriz[2][3] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #meio(matriz[1][3])
    elif j1 == 1 and j2 == 3:
        if matriz[0][2] == bomba:
            contador_bombas += 1
        if matriz[0][3] == bomba:
            contador_bombas += 1
        if matriz[0][4] == bomba:
            contador_bombas += 1
        if matriz[1][2] == bomba:
            contador_bombas += 1
        if matriz[1][4] == bomba:
            contador_bombas += 1
        if matriz[2][2] == bomba:
            contador_bombas += 1
        if matriz[2][3] == bomba:
            contador_bombas += 1
        if matriz[2][4] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #meio(matriz[1][4])
    elif j1 == 1 and j2 == 4:
        if matriz[0][3] == bomba:
            contador_bombas += 1
        if matriz[0][4] == bomba:
            contador_bombas += 1
        if matriz[0][5] == bomba:
            contador_bombas += 1
        if matriz[1][3] == bomba:
            contador_bombas += 1
        if matriz[1][5] == bomba:
            contador_bombas += 1
        if matriz[2][3] == bomba:
            contador_bombas += 1
        if matriz[2][4] == bomba:
            contador_bombas += 1
        if matriz[2][5] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #meio(matriz[2][1])
    elif j1 == 2 and j2 == 1:
        if matriz[1][0] == bomba:
            contador_bombas += 1
        if matriz[1][1] == bomba:
            contador_bombas += 1
        if matriz[1][2] == bomba:
            contador_bombas += 1
        if matriz[2][0] == bomba:
            contador_bombas += 1
        if matriz[2][2] == bomba:
            contador_bombas += 1
        if matriz[3][0] == bomba:
            contador_bombas += 1
        if matriz[3][1] == bomba:
            contador_bombas += 1
        if matriz[3][2] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #meio(matriz[2][2])
    elif j1 == 2 and j2 == 2:
        if matriz[1][1] == bomba:
            contador_bombas += 1
        if matriz[1][2] == bomba:
            contador_bombas += 1
        if matriz[1][3] == bomba:
            contador_bombas += 1
        if matriz[2][1] == bomba:
            contador_bombas += 1
        if matriz[2][3] == bomba:
            contador_bombas += 1
        if matriz[3][1] == bomba:
            contador_bombas += 1
        if matriz[3][2] == bomba:
            contador_bombas += 1
        if matriz[3][3] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #meio(matriz[2][3])
    elif j1 == 2 and j2 == 3:
        if matriz[1][2] == bomba:
            contador_bombas += 1
        if matriz[1][3] == bomba:
            contador_bombas += 1
        if matriz[1][4] == bomba:
            contador_bombas += 1
        if matriz[2][2] == bomba:
            contador_bombas += 1
        if matriz[2][4] == bomba:
            contador_bombas += 1
        if matriz[3][2] == bomba:
            contador_bombas += 1
        if matriz[3][3] == bomba:
            contador_bombas += 1
        if matriz[3][4] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')

    #meio(matriz[2][4])
    elif j1 == 2 and j2 == 4:
        if matriz[1][3] == bomba:
            contador_bombas += 1
        if matriz[1][4] == bomba:
            contador_bombas += 1
        if matriz[1][5] == bomba:
            contador_bombas += 1
        if matriz[2][3] == bomba:
            contador_bombas += 1
        if matriz[2][5] == bomba:
            contador_bombas += 1
        if matriz[3][3] == bomba:
            contador_bombas += 1
        if matriz[3][4] == bomba:
            contador_bombas += 1
        if matriz[3][5] == bomba:
            contador_bombas += 1
        if contador_bombas > 0:
            print(contador_bombas)
        else:
            print('X')