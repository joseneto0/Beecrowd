s,t,f = map(int, input().split())
hora = s + t + f
if hora >= 24:
    hora = hora - 24
elif hora < 0:
    hora = 24 + hora
print(hora)