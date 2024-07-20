import math

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    tmp = arr[1:]
    ans = 0
    for i in range(len(tmp)-1):
        for j in range(i+1, len(tmp)):
            ans += math.gcd(tmp[i], tmp[j])
    print(ans)