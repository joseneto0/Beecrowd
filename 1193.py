n = int(input())
for i in range(n):
    num, formato = input().split()
    if formato == 'bin':
        print(f"Case {i+1}:")
        num = int(num, 2)
        print(num, "dec")
        hex_num = format(num, 'x')
        print(hex_num, "hex")
        print()
    elif formato == "dec":
        print(f"Case {i+1}:")
        hex_num = format(int(num), 'x')
        print(hex_num, "hex")
        print(format(int(num), 'b'), "bin")
        print()
    else:
        print(f"Case {i+1}:")
        dec_num = int(num, 16)
        print(dec_num, "dec")
        bin_num = format(dec_num, 'b')
        print(bin_num, "bin")
        print()