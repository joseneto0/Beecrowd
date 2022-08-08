n = int(input())
for i in range(n):
    h, m, o = map(int, input().split())
    if h < 10:
        h = str(h)
        h = '0' + h
    if m < 10:
        m = str(m)
        m = '0' + m
    if o == 1:
        print(f'{h}:{m} - A porta abriu!')
    else:
        print(f'{h}:{m} - A porta fechou!')