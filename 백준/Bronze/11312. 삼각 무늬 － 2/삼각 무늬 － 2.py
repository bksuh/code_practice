n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(pow(a//b,2))