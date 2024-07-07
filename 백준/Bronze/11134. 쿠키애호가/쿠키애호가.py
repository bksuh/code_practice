n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if not a%b:
        print(a//b)
    else:
        print((a//b)+1)