n = int(input())
for _ in range(n):
    a, b=input().split()
    print("Distances: ", end='')
    for i in range(len(a)):
        tmp = ord(b[i]) - ord(a[i])
        if tmp<0:
            tmp +=26
        print(tmp, end=' ')
    print()