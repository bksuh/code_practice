import sys
import collections
input = sys.stdin.readline

a1 = set()
a2 = set()
n, m = map(int, input().split())
for _ in range(n):
    a = input().rstrip()
    a1.add(a)

for _ in range(m):
    b = input().rstrip()
    a2.add(b)

tmp = list(a1.intersection(a2))
tmp.sort()
print(len(tmp))
for element in tmp:
    print(element)