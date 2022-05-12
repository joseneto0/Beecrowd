total = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0
num = int(input())
for i in range(num):
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = str(n2).upper()
    total += n1
    if n2 == 'C':
        total_coelhos += n1
    elif n2 == 'R':
        total_ratos += n1
    elif n2 == 'S':
        total_sapos += n1
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(total_coelhos))
print('Total de ratos: {}'.format(total_ratos))
print('Total de sapos: {}'.format(total_sapos))
porcentagem_coelhos = (total_coelhos * 100) / total
porcentagem_ratos = (total_ratos * 100) / total
porcentagem_sapos = (total_sapos * 100) / total
print('Percentual de coelhos: {:.2f} %'.format(porcentagem_coelhos))
print('Percentual de ratos: {:.2f} %'.format(porcentagem_ratos))
print('Percentual de sapos: {:.2f} %'.format(porcentagem_sapos))