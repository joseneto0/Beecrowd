##s = segundos do input
s = int(input())
horas = s // 3600
s = s - horas * 3600
minutos = s // 60
s = s - minutos * 60
##segundos da resposta
segundos = s
print('{}:{}:{}'.format(horas, minutos, segundos))
