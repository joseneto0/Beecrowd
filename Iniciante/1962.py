n = int(input())
for i in range(n):
    anos = int(input())
    if anos <= 2014:
        print(f"{2014+1-anos} D.C.")
    else:
        print(f"{anos - 2014} A.C.")