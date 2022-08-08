joias = []
while True:
    try:
        joias.append(input())
    except EOFError:
        break
print(len(set(joias)))