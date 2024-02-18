n = int(input())
for i in range(n):
    m = int(input())
    l = list(map(int, input().split()))
    k = l.copy()
    l.sort(reverse=True)
    r = 0
    for i in range(m):
        if l[i] == k[i]:
            r += 1
    print(r)