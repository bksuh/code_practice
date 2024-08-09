a, b, c = map(int, input().split())
d = {}
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            tmp = i + j + k
            if tmp in d:
                d[tmp] +=1
            else:
                d[tmp] = 1
ans = [(k,v) for k,v in d.items()]
ans.sort(key= lambda x: (-x[1], x[0]))
print(ans[0][0])