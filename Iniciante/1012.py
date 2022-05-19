val = input() .split(' ')
A = float(val[0])
B = float(val[1])
C = float(val[2])
triangulo = (A * C) / 2
circulo = 3.14159 * (C**2)
trapezio = (A + B) / 2 * C
quadrado = B * B
retângulo = A * B
print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retângulo:.3f}')