import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    b, p = map(float, input().split())
    cal = 60*b/p
    gap = 60/p
    print("%.4f %.4f %.4f" %(cal-gap, cal,cal +gap))