t = int(input())
price = [int(input()) for _ in range(t)]

cost = 0
n = int(input())
for _ in range(n):
    a = int(input())
    cost += price[a-1]
print(cost)
