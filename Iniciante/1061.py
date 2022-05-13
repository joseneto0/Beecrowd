dia1 = input().split(' ')
dia_inicial = int(dia1[1])
hrs1 = input().split(' ')
hora_inicial = int(hrs1[0])
minuto_inicial = int(hrs1[2])
segundo_inicial = int(hrs1[4])

dia2 = input().split(' ')
dia_final = int(dia2[1])
hrs2 = input().split(' ')
hora_final = int(hrs2[0])
minuto_final = int(hrs2[2])
segundo_final = int(hrs2[4])

dias = dia_final - dia_inicial

horas = hora_final - hora_inicial
if horas < 0:
    horas += 24
    dias -= 1

minutos = minuto_final - minuto_inicial
if minutos < 0:
    minutos += 60
    horas -= 1

segundos = segundo_final - segundo_inicial
if segundos < 0:
    segundos += 60
    minutos -= 1

if dias <= 0:
    dias = 0

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')