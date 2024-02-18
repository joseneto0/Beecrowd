n = int(input())
for i in range(n):
    nova_string = ''
    string = input()
    metade = int(len(string) / 2)
    for i in range(metade-1, -1, -1):
        nova_string += string[i]
    for i in range(len(string)-1, metade-1, -1):
        nova_string += string[i]
    print(nova_string)