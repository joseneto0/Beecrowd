while True:
    try:
        n = input()
        n = list(n)
        i = 0
        while i < len(n):
            if n[i] == '(':
                for k in range(i, len(n)):
                    if n[k] == ')':
                        n[i] = '0'
                        n[k] = '0'
                        break
            i += 1
        for i in n:
            if i == '(' or i == ')':
                print('incorrect')
                break
        else:
            print('correct')
    except EOFError:
        break