import sys
input = sys.stdin.readline
n = int(input())
ans = 0

for i in range(n-1):
    tmp = int(input())
    ans = ans - 1 + tmp

last = int(input())
ans = last + ans
print(ans)