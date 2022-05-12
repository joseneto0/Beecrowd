valor = int(input())
for i in range(valor):
    valores = int(input())
    if valores < 0 and valores % 2 == 0:
        print('EVEN NEGATIVE')
    elif valores == 0:
        print('NULL')
    elif valores > 0 and valores % 2 == 0:
        print('EVEN POSITIVE')
    elif valores < 0 and valores % 2 != 0:
        print('ODD NEGATIVE')
    elif valores > 0 and valores % 2 != 0:
        print('ODD POSITIVE')