n = int(input())
rep = 0
while rep < n:
    string = input()
    numerosFinais = ''
    if len(string) == 8:
        for i in range(3):
            if string[i] >= "A" and string[i] <= "Z":
                continuar = True
            else:
                continuar = False
        if string[3] == '-':
            continuar == True
        else:
            continuar = False
        if continuar == True:
            numerosFinais = string[4:]
            if numerosFinais.isdigit():
                if numerosFinais[3] == '1' or numerosFinais[3] == '2':
                    print('MONDAY')
                elif numerosFinais[3] == '3' or numerosFinais[3] == '4':
                    print('TUESDAY')
                elif numerosFinais[3] == '5' or numerosFinais[3] == '6':
                    print('WEDNESDAY')
                elif numerosFinais[3] == '7' or numerosFinais[3] == '8':
                    print('THURSDAY')
                elif numerosFinais[3] == '9' or numerosFinais[3] == '0':
                    print('FRIDAY')
            else:
                print('FAILURE')
        else:
            print('FAILURE')
    else:
        print('FAILURE')
    rep += 1