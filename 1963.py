N = int(input())
binario = []
octal = []
hexadecimal = []

#binario
N_binario = N
while N_binario != 0:
    resto_binario = N_binario % 2
    N_binario //= 2
    binario.append(resto_binario)
binario.reverse()

#octal
N_octal = N
while N_octal != 0:
    resto_octal = N_octal % 8
    N_octal //= 8
    octal.append(resto_octal)
octal.reverse()

#hexadecimal
N_hexadecimal = N
while N_hexadecimal != 0:
    if N_hexadecimal % 16 < 10:
        hexadecimal.append(N_hexadecimal % 16)
    elif N_hexadecimal % 16 == 10:
        hexadecimal.append('A')
    elif N_hexadecimal % 16 == 11:    
        hexadecimal.append('B')
    elif N_hexadecimal % 16 == 12:
        hexadecimal.append('C')
    elif N_hexadecimal % 16 == 13:    
        hexadecimal.append('D')
    elif N_hexadecimal % 16 == 14:    
        hexadecimal.append('E')
    elif N_hexadecimal % 16 == 15:    
        hexadecimal.append('F')
    N_hexadecimal //= 16
hexadecimal.reverse()

for b in range(len(binario)):
    print(binario[b], end='')
if N == 0:
    print(0)
else:
    print()

for o in range(len(octal)):
    print(octal[o], end='')
if N == 0:
    print(0)
else:
    print()

for h in range(len(hexadecimal)):
    print(hexadecimal[h], end='')
if N == 0:
    print(0)
else:
    print()