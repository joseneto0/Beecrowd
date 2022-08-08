n = int(input())
for i in range(n):
    string = input().split()
    s = ''
    for i in range(len(string)):
        s += string[i][0]
    print(s)
    s = ''