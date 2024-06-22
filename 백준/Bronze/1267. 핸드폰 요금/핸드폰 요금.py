import sys
input = sys.stdin.readline

n =  int(input())
arr = list(map(int, input().split()))
y, m = 0, 0

for i in range(len(arr)):
    y +=10*((arr[i]//30)+1)
    m +=15*((arr[i]//60)+1)


if y ==m:
    print('Y', 'M', y)
elif y>m:
    print('M', m)
else:
    print('Y', y)