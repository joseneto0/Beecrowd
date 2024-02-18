a, b, c = map(int, input().split())
if a + b == c or a + c == b or b + c == a or a - b == 0 or b - a == 0 or a - c == 0 or c - a == 0 or b - c == 0 or c - b == 0:
    print('S')
else:
    print('N')