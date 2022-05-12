testes = int(input())
primeiro_peso = 2
segundo_peso = 3
terceiro_peso = 5
for i in range(testes):
    nota_1, nota_2, nota_3 = map(float, input().split())
    media_1 = (nota_1 * primeiro_peso + nota_2 * segundo_peso + nota_3 * terceiro_peso) / (primeiro_peso + segundo_peso + terceiro_peso)
    print('{:.1f}'.format(media_1))
    media_1 = (nota_1 * primeiro_peso + nota_2 * segundo_peso + nota_3 * terceiro_peso) / (primeiro_peso + segundo_peso + terceiro_peso)
    print('{:.1f}'.format(media_1))
    media_1 = (nota_1 * primeiro_peso + nota_2 * segundo_peso + nota_3 * terceiro_peso) / (primeiro_peso + segundo_peso + terceiro_peso)
    print('{:.1f}'.format(media_1))