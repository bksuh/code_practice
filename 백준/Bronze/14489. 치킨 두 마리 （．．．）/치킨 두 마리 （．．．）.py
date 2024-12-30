a, b = list(map(int, input().split()))
C = int(input())
if a + b >= 2 * C:
    print(a + b - (2 * C))
else:
    print(a + b)