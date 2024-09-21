import sys
input = sys.stdin.readline
tmp = ["A",'E', 'I', "O",'U','a','e','i','o','u']
t = int(input())

for _ in range(t):
    ans = input().rstrip()
    cnt = 0
    for c in ans:
        if c in tmp:
            cnt+=1
    print(len(ans)-ans.count(' ')-cnt, cnt)
    