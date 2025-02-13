t = int(input())

a = '++++ '
b = '|'

for _ in range(t):
    n = int(input())
    x = n //5
    y = n % 5
    print(a*x + b*y)