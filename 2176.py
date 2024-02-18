n = input()
if n.count('1') % 2 == 0:
    n += '0'
else:
    n += '1'
print(n)