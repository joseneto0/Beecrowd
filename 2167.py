n = int(input())
r = list(map(int,input().split()))
pos = 0
for i in range(len(r)):
    if i > 0:
         if r[i] < r[i-1]:
             pos = i + 1
             break
print(pos)
