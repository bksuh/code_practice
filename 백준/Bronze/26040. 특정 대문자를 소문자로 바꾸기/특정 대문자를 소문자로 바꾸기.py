t = input()
ans = ''
picks = list(input().split())

for c in t:
    if c in picks:
        ans += c.lower()
    else:
        ans += c
print(ans)