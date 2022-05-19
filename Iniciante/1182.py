valores = []
soma = 0
media = 0
for i in range(12):
    valores.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

coluna = int(input())
operacao = input()
for l in range(12):
    for c in range(12):
        valores[l][c] = float(input())
        if c == coluna and operacao == 'S':
            soma += valores[l][coluna]
        elif c == coluna and operacao == 'M':
            soma += valores[l][coluna]
            media = soma / 12
if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    print(f'{media:.1f}')