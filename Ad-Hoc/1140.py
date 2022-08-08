while True:
    string = input().lower()
    if string == '*':
        break
    string = string.split()
    s = string[0][0]
    certo = None
    for i in range(len(string)):
        if string[i][0] == s:
            certo = True
        else:
            certo = False
            break
    if certo == True:
        print('Y')
    else:
        print('N')