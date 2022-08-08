while True:
    n = input()
    try:
        n = int(n)
        if n < 0:
            break
        else:
            hex_num = str(hex(n))
            s = ''
            for i in hex_num:
                if i.isdigit() == False and i != 'x':
                    s += i.upper()
                else:
                    s += i
            print(s)
    except:
        print(int(n, 16))