while True:
    try:
        v = float(input())
        d = float(input())
        raio = d / 2
        altura = v / (3.14 * (raio ** 2))
        area = 3.14 * raio**2
        print(f"ALTURA = {altura:.2f}")
        print(f"AREA = {area:.2f}")
    except EOFError:
        break