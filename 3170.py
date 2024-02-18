b = int(input())
g = int(input())
if g % 2 == 0:
    if g/2 <= b:
        print('Amelia tem todas bolinhas!')
    else:
        print(f"Faltam {g/2 - b:.0f} bolinha(s)")
else:
    while g % 2 != 0:
        g -= 1
    if g/2 <= b:
        print('Amelia tem todas bolinhas!')
    else:
        print(f"Faltam {g/2 - b:.0f} bolinha(s)")