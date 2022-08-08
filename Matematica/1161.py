from math import factorial
while True:
    try:
        a, b = map(int, input().split())
        print(factorial(a) + factorial(b))
    except EOFError:
        break