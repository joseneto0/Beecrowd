n = int(input())
for i in range(n):
    n = input()
    n = list(n)
    j = 0
    cont = 0
    while j < len(n):
        if n[j] == '<':
            for k in range(j, len(n)):
                if n[k] == '>':
                    cont += 1
                    n[j] = 0
                    n[k] = 0
                    break
        j += 1
    print(cont)