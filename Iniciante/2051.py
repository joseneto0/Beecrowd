valor = ''
N = int(input())
while True:
    valor += str(N)
    N = int(input())
    if N > 1 or N < 0:
        break
valor_int = int(valor)
decimal = int(valor, 2)
print(valor) 
print(decimal)