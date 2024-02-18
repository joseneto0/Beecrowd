while True:
    try:
        frase = input()
        n = int(input())
        numeros = list(map(int,input().split()))
        string = ''
        for i in numeros:
            string += frase[i-1]
        print(string)
    except EOFError:
        break