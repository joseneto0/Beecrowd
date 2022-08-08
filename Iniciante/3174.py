n = int(input())
somaBonecos = somaArquitetos = somaMusicos = somaDesenhistas = 0
for i in range(n):
    E, G, H = input().split()
    H = int(H)
    if G == "bonecos":
        somaBonecos += H
    elif G == 'arquitetos':
        somaArquitetos += H
    elif G == 'musicos':
        somaMusicos += H
    elif G == 'desenhistas':
        somaDesenhistas += H
print((somaBonecos // 8) + (somaArquitetos // 4) + (somaMusicos // 6) + (somaDesenhistas // 12))