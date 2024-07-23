a, b = map(int, input().split())
ans = 1
for i in range(a, b+1):
    tmp = [c for c in range(1, i+1)]
    ans *= sum(tmp)

print(ans%14579)