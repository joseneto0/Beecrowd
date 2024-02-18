n = int(input())

anos = n // 365
r = n % 365

mes = r // 30
r = r % 30

dias = r

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dias))