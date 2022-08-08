n = int(input())
dict = {}
rep = 0
while rep < n:
    t = int(input())
    for i in range(t):
        idioma = input()
        if idioma not in dict:
            dict[idioma] = 0
            dict[idioma] += 1
        else:
            dict[idioma] += 1
    if len(dict) >= 2:
        print('ingles')
    else:
        print(idioma)
    dict = {}
    rep += 1