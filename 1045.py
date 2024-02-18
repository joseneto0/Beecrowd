n1, n2, n3 = map(float, input().split())
if n1 >= n2 and n1 >= n3:
    A = n1
    B = n2
    C = n3
elif n2 >= n1 and n2 >= n3:
    A = n2
    B = n1
    C = n3
elif n3 >= n1 and n3 >= n2:
    A = n3
    B = n1
    C = n2
if A >= B + C:
    print('NAO FORMA TRIANGULO')
elif (A ** 2 == B ** 2 + C ** 2):
    print('TRIANGULO RETANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B and A != C or B == C and B != A or A == C and A != B:
        print('TRIANGULO ISOSCELES')
elif (A ** 2 > B ** 2 + C ** 2):
    print('TRIANGULO OBTUSANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B and A != C or B == C and B != A or A == C and A != B:
        print('TRIANGULO ISOSCELES')
elif (A ** 2 < B ** 2 + C ** 2):
    print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B and A != C or B == C and B != A or A == C and A != B:
        print('TRIANGULO ISOSCELES')
