from math import ceil
while True:
    try:
        numero = int(input())
        print(ceil(numero / 100.0))
    except EOFError:
        break