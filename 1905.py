T = int(input())
print()
grafo = {

}
for i in range(2):
    for j in range(5):
        l = list(map(int, input().split()))
        for k in range(4):
            if l[k] == 0 and l[k+1] == 0:
                grafo[k+j] = [k+1]
    print()
    