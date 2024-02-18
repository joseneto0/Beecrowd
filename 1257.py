import string
n = int(input())
rep = rep1 = qtd = 0
alfabeto = string.ascii_uppercase
while rep < n: 
    l = int(input())
    while rep1 < l:
        string = input()
        for i in range(len(string)):
            qtd += alfabeto.index(string[i]) + rep1 + i
        rep1 += 1
    print(qtd)
    qtd = 0
    rep += 1
    rep1 = 0