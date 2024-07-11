a,b,c = map(int, input().split())
price = [0, a, b, c]

car = [0 for _ in range(100)]
tmp = 1
for _ in range(3):
    x, y = map(int, input().split())
    tmp = max(tmp, y)
    for i in range(x-1, y-1):
        car[i] +=1
ans = 0
for i in range(tmp):
    ans += price[car[i]]*car[i]
print(ans)