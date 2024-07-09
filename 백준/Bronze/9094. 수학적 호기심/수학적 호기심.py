import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m = map(int, input().rstrip().split())
    cnt = 0
    for i in range(1,n):
        for j in range(i+1, n):
            if (pow(i,2)+pow(j,2)+m)%(i*j) ==0:
                cnt+=1
    print(cnt)