maiores = []
N = int(input())
while True:
    maiores.append(N)
    N = int(input())
    if N == 0:
        break
for i in range(len(maiores)):
    if maiores[i] > maiores[len(maiores) - 1]:
        print(maiores[i])