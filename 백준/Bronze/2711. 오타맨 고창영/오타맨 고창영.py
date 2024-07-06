n = int(input())
for _ in range(n):
    a, b = input().split()
    a = int(a)-1
    print(b[:a]+b[a+1:])