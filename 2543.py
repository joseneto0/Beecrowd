while True:
    try:
        n, i1 = input().split()
        cs = 0
        for i in range(int(n)):
            i2, j2 = input().split()
            if i2 == i1 and j2 == '0':
                cs += 1
        print(cs) 
    except EOFError:
        break