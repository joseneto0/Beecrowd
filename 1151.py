num = int(input())
primeiro = 0
segundo = 1
contador = 3
print(f'{primeiro} {segundo} ', end='')
while contador <= num:
    terceiro = primeiro + segundo
    if contador < num:
        print(f'{terceiro}' , end=' ')
    elif contador == num:
        print(terceiro)
    contador += 1
    primeiro = segundo
    segundo = terceiro