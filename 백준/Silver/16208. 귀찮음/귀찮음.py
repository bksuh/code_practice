import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
arr.sort()
for _ in range(n-1):
    ans += (arr[-1] * (sum(arr)- arr[-1]))
    arr.pop()
print(ans)
