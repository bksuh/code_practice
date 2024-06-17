import sys
input = sys.stdin.readline

result = [1, 1, 2, 2, 2, 8]
ans = list(map(int, input().split()))

for i in range(len(ans)):
    ans[i] = result[i] - ans[i]
print(*ans)