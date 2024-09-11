n = int(input())
ice = list(map(int, input().split()))
left, right = [], []
indi = False
for c in ice:
    if c == -1:
        indi = True
        continue
    if not indi:
        left.append(c)
    else:
        right.append(c)

ans = min(left) + min(right)
print(ans)
    