a =[350.34, 230.90, 190.55, 125.30, 180.90]
n = int(input())

for _ in range(n):
    b = list(map(int, input().split()))
    price = 0
    for i in range(len(b)):
        price += (a[i]*b[i])
    print(f"${price:.2f}")