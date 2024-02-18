while True:
    try:
        a,b = map(int,input().split(':'))
        minutos = (a * 60) + b
        if minutos + 60 > 480:
            print(f"Atraso maximo: {minutos+60-480}")
        else:
            print(f"Atraso maximo: 0")
    except EOFError:
        break