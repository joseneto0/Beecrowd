frase = input()
virgula = frase.index(',')
s = ''
for i in range(virgula):
    s += frase[i]
print(s)
s = ''
for i in range(virgula+1, len(frase)):
    s += frase[i]
print(s)