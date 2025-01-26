hr = int(input())
ans = 0
if 20 <= hr <= 23:
    ans += (24 -hr)
else:
    ans -= hr

m = int(input())
ans += m

print(ans)