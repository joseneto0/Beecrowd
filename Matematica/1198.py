while True:
    try:
        h, o = map(int, input().split())
        print(abs(h - o))
    except EOFError:
        break