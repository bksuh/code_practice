a, b, c, d = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for elem in range(max(arr)+1):
    cnt = 0
    if elem % (a+b) < a:
        cnt += 1
    if elem % (c+d) < c:
        cnt += 1
    ans.append(cnt)
for elem in arr:
    print(ans[elem-1])
