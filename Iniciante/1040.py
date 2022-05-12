N1, N2, N3, N4 = input().split()
N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)
media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10
if media >= 7.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
else:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    notaexame = float(input())
    print('Nota do exame: {:.1f}'.format(notaexame))
    mediafinal = (notaexame + media) / 2 
    if mediafinal >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(mediafinal))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(mediafinal))