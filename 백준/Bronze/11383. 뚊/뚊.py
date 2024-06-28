import sys
input = sys.stdin.readline

n, m = map(int, input().split())
in1 = list(input().rstrip() for _ in range(n))
out1 = list(input().rstrip() for _ in range(n))
arr1 = []
for i in range(len(in1)):
    tmp = ''
    for j in range(len(in1[i])):
        tmp+=2*in1[i][j]
    arr1.append(tmp)

if arr1 == out1:
    print('Eyfa')
else:
    print('Not Eyfa')