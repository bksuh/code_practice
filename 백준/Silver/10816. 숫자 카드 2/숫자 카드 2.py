import sys
input = sys.stdin.readline

n = int(input())
arrn = list(map(int, input().split()))
m = int(input())
arrm = list(map(int, input().split()))
d = {}

for element in arrm:
    d[element] = 0
for element in arrn:
    if element in d:
        d[element] +=1
for i in arrm:
    print(d[i], end = ' ')