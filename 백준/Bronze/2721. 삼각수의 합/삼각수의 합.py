n = int(input())
for _ in range(n):
    n = int(input())
    sum = 0
    for k in range(1, n+1):
        sum +=((k+1)*(k+2)*k//2)
    print(sum)