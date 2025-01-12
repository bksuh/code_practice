a, b, c = map(int, input().split())
total = a + b 
ans = 0

while total >= c:
    ans += total//c
    total = total//c + total%c

print(ans)