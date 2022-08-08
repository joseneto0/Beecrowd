n = int(input())
alunos = []
notas = []
continuar = True
for i in range(n):
    a, n = input().split()
    a, n = int(a), float(n)
    alunos.append(a)
    notas.append(n)
maior = max(notas)
if maior >= 8:
    index_maior = notas.index(max(notas))
    aluno_apto = alunos[index_maior]
    print(aluno_apto)
else:
    print("Minimum note not reached")