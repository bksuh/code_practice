import sys
input = sys.stdin.readline

n = int(input())
ans = 1
while True:
    if 3*ans*(ans-1) +1 >= n:
        print(ans)
        break
    ans+=1