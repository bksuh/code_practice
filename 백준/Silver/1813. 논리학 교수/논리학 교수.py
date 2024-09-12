n = int(input())
arr = list(map(int, input().split()))

from collections import Counter
ans = -1
tmp = Counter(arr)
for k, v in tmp.items():
    if k != v:
        continue
    else:
        ans = max(ans,k)
if ans == -1 and arr.count(0) == 0:
    print(0)
else:
    print(ans)