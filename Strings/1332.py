num = int(input())
one = 'one'
two = 'two'
three = 'three'
qntd = 1
while qntd <= num:
    count = 0
    string = input()
    if len(string) == len(one):
        for i in range(len(string)):
            if string[i] != one[i]:
                count += 1
        if count <= 1:
            print(1)
    count = 0
    if len(string) == len(two):
        for i in range(len(string)):
            if string[i] != two[i]:
                count += 1
        if count <= 1:
            print(2)
    elif len(string) == len(three):
        for i in range(len(string)):
            if string[i] != three[i]:
                count += 1
        if count <= 1:
            print(3)
    qntd += 1