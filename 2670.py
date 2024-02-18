lista = []
tempo = 0
for i in range(3):
    lista.append(int(input()))
p1 = lista[0] * 0 + lista[1] * 2 + lista[2] * 4
p2 = lista[0] * 2 + lista[1] * 0 + lista[2] * 2
p3 = lista[0] * 4 + lista[1] * 2 + lista[2] * 0
if p1 <= p2:
    result = p1
else:
    result = p2
if result >= p3:
    result = p3
print(result)