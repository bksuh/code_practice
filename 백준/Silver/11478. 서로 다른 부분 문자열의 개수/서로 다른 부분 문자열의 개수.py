import itertools

ans = []
tar = input()
for k in range(len(tar)):
    for j in range(k, len(tar)):
        tmp = tar[k:j+1]
        ans.append(tmp)
ans = set(ans)
print(len(ans))