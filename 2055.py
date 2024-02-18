frase = input().upper()
st = 'AEIOU'
print(frase)
for i in range(len(st)):
    for j in range(len(frase)):
        if frase[j] in st:
            print(st[i],end='')
        else:
            print(frase[j],end='')
    print()