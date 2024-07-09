n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    par = a + b*d
    nopar = b*c
    if par == nopar:
        print("does not matter")
    elif par < nopar:
        print("parallelize")
    else:
        print('do not parallelize')