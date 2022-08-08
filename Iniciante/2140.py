while True:
    notas = [100,50,20,10,5,2]
    count = 0
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    conta = b - a
    for i in notas:
        if conta // i == 1:
            conta -= i
            count += 1
    if count == 2:
        print('possible')
    else:
        print('impossible')
    count = 0