while True:
    try:
        h, m = map(int, input().split())
        hora = (h // 15) // 2
        minutos = m / 60
        hora = str(hora)
        minutos = str(minutos)
        minutos = minutos.replace('.', '')
        if len(hora) == 1:
            horaFinal = '0' + hora
        else:
            horaFinal = hora
        if len(minutos) == 1:
            minutoFinal = '0' + minutos
        else:
            minutoFinal = minutos
        print(f"{horaFinal}:{minutoFinal}")
        minutoFinal = ''
        horaFinal = ''
    except EOFError:
        break