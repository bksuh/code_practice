a, b, c = map(int, input().split())
tmp = pow(b**2 + c**2, 1/2)
for _ in range(a):
    x = int(input())
    print('DA' if x<=tmp else 'NE')