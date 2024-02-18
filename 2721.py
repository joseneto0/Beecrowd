renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']
bolasNeves = list(map(int, input().split()))
soma = sum(bolasNeves)
r = 0
for i in range(soma):
    if r == 8:
        r = 0
    else:
        r += 1
print(renas[r-1])