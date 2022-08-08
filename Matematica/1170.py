n = int(input())
for i in range(n):
    num = float(input())
    cont = 0
    while num > 1:
        num = num / 2
        cont += 1
    print(cont, "dias")