frase = input()
print(frase)

for i in frase:
    if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
        if i == 'z':
            i = i.replace('z', '`')
        else:
            i = i.replace('Z', '@')
        print(i.replace(i, chr(ord(i) + 1)), end='')
    else:
        print(i,end='')
print()