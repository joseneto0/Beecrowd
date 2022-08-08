def verificar(agora, pulo, altura):
    if abs(agora - pulo) > p:
        return False
    else:
        return True


p, n = map(int, input().split())
alturas = list(map(int, input().split()))
for i in range(n-1):
    continuar = verificar(alturas[i], alturas[i+1], p)
    if continuar == False:
        print("GAME OVER")
        break
if continuar == True:
    print("YOU WIN")