qntd_grenais = 0
vitoria_inter = 0
vitoria_gremio = 0
empate = 0
while True:
    inter, gremio = map(int, input().split())
    qntd_grenais += 1
    if inter > gremio:
        vitoria_inter += 1
    elif gremio > inter:
        vitoria_gremio += 1
    else:
        empate += 1
    print('Novo grenal (1-sim 2-nao)')
    novo = int(input())
    if novo == 2:
        break
print(f'{qntd_grenais} grenais')
print(f'Inter:{vitoria_inter}')
print(f'Gremio:{vitoria_gremio}')
print(f'Empates:{empate}')
if vitoria_inter > vitoria_gremio:
    print('Inter venceu mais')
elif vitoria_gremio > vitoria_inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')