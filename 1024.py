n = int(input())
string_nova = string_final = ''
for i in range(n):
    string = input()
    for i in range(len(string)):
        if string[i].isalpha() == True:
            string_nova += chr(ord(string[i]) + 3)
        else:
            string_nova += string[i]
    string_nova = string_nova[::-1]
    metade = len(string_nova) // 2
    for i in range(metade):
        string_final += string_nova[i]
    for i in range(metade, len(string_nova)):
        string_final += chr(ord(string_nova[i]) - 1)
    print(string_final)
    string_nova = string_final = ''