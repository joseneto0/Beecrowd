n = int(input())
for i in range(n):
    nome1, jogada1_string, nome2, jogada2_string = input().split()
    jogada1, jogada2 = map(int, input().split())
    soma = jogada1 + jogada2
    if soma % 2 == 0 and jogada1_string == "PAR":
        print(nome1)
    elif soma % 2 == 0 and jogada1_string == "IMPAR":
        print(nome2)
    elif soma % 2 != 0 and jogada1_string == "PAR":
        print(nome2)
    elif soma % 2 != 0 and jogada1_string == "IMPAR":
        print(nome1)
