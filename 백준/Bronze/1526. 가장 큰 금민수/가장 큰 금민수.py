n = int(input())
ans = 0

for i in range(1, n+1):
    indi = False
    for c in str(i):
        if c == '4' or c == '7':
            indi = True
        else:
            indi = False
            break
    if not indi:
        continue
    ans = i
print(ans)