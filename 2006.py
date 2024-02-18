n = int(input())
cha = list(map(int, input().split()))
correct = 0
for i in cha:
    if i == n:
        correct += 1
print(correct)