import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
tmp = list(set(a))
tmp.sort()
print(*tmp)