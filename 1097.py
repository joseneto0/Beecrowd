i = 1
j = 7
while i <= 9:
    for rep in range(1, 4):
        print('I={} J={}'.format(i,j))
        j -= 1
    i += 2
    j += 5