hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

minuto_inicial += hora_inicial * 60
minuto_final += hora_final * 60

total = minuto_final - minuto_inicial
if total <= 0:
    total += 24 * 60

horas = total // 60

minutos = total % 60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))