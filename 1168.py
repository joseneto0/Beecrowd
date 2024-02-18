N = int(input())
for i in range(N):
    leds = 0
    valores = input()
    for j in range(len(valores)):
        if valores[j] == '1':
            leds += 2
        elif valores[j] == '2' or valores[j] == '3' or valores[j] == '5':
            leds += 5
        elif valores[j] == '4':
            leds += 4
        elif valores[j] == '6' or valores[j] == '9' or valores[j] == '0':
            leds += 6
        elif valores[j] == '7':
            leds += 3
        elif valores[j] == '8':
            leds += 7
    print(f'{leds} leds')