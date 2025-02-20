a, b = map(int, input().split())

increment = a-1
delta = a - 2
ans = a

for _ in range(b-1):
    increment = increment+delta
    ans += increment
print(ans)