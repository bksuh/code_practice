n = int(input())
for i in range(n):
    price = int(input())
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        price +=(a*b)
    print(price)