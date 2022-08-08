while True:
    try:
        n = int(input())
        rep = 0
        while n > 1:
            n //= 2
            rep += 1
        print(rep)
    except EOFError:
        break