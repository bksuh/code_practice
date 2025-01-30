a, b = map(int, input().split())

tar = [(i, v) for i, v in enumerate(input())]
tar.sort(key = lambda x: (x[1], x[0]))
tar = tar[b:]
tar.sort(key=lambda x : (x[0]))

ans = ''
for i in range(len(tar)):
    ans += tar[i][1]
print(ans)