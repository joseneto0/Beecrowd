salida = []
vuelta = []
while True:
    s = list(input().split())
    if s[0] == 'ABEND':
        break
    t = int(s[1])
    if s[0] == 'SALIDA':
        salida.append(t)
    else:
        vuelta.append(t)
print(abs(sum(salida) - sum(vuelta)))
print(abs(len(salida) - len(vuelta)))