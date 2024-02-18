cord_i_1 = cord_j_1 = cord_i_2 = cord_j_2 = 0
while True:
    try:
        n, m = map(int, input().split())
        matriz = []
        for i in range(n):
            matriz.append(input().split())
        for i in range(n):
            for j in range(m):
                if '1' in matriz[i][j]:
                    cord_i = i
                    cord_j = j
                if '2' in matriz[i][j]:
                    cord_i_2 = i
                    cord_j_2 = j
        if cord_i > cord_i_2:
            coordenada_1 = cord_i - cord_i_2
        else:
            coordenada_1 = cord_i_2 - cord_i
        if cord_j > cord_j_2:
            coordenada_2 = cord_j - cord_j_2
        else:
            coordenada_2 = cord_j_2 - cord_j
        print(coordenada_1 + coordenada_2)
    except EOFError:
        break