posicao = 0
N = int(input())
lista = list(map(int, input().split()))
print(f'Menor valor: {min(lista)}')
print(f'Posicao: {lista.index(min(lista))}')