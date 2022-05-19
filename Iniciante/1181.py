valores = []
soma = 0
media = 0
for i in range(12):
    valores.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

linha = int(input())
operacao = input()
for l in range(12):
    for c in range(12):
        valores[l][c] = float(input())
        if l == linha and operacao == 'S':
            soma += valores[linha][c]
        elif l == linha and operacao == 'M':
            soma += valores[linha][c]
            media = soma / 12
if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    print(f'{media:.1f}')