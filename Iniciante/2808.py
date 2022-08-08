a, b = input().split()
num1 = int(a[1])
num2 = int(b[1])
l1 = a[0]
l2 = b[0]
if chr(ord(l2) + 2) == chr(ord(l1)) or chr(ord(l2) - 2) == chr(ord(l1)) or chr(ord(l2) + 1) == chr(ord(l1)) and abs(num2 - num1) == 2 or chr(ord(l2) - 1) == chr(ord(l1)) and abs(num2 - num1) == 2:
    print('VALIDO')
else:
    print('INVALIDO')