n = int(input())
string_nova = ''
rep = 0
while rep < n:
    string = input()
    casas = int(input())
    for i in range(len(string)):
        pos = ord(string[i]) - casas
        if pos < 65:
            string_nova += chr(91 - (65 - pos))
        else:
            string_nova += chr(ord(string[i]) - casas)
    print(string_nova)
    string_nova = ''
    rep += 1