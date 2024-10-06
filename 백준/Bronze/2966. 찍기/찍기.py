n = int(input())
a = 'ABC' * (n//3 + 1)
b = 'BABC' * (n//4 + 1)
c = 'CCAABB' * (n//6 + 1)

compare = input()
score = [0, 0, 0]
for i in range(len(compare)):
    if compare[i] == a[i]:
        score[0] += 1
    if compare[i] == b[i]:
        score[1] += 1
    if compare[i] == c[i]:
        score[2] += 1
result = {}
for i, v in enumerate(['Adrian', 'Bruno', 'Goran']):
    if score[i] in result.keys():
        result[score[i]].append(v)
    else:
        result[score[i]] = [v]
ans = max(result.keys())
print(ans)
print(*result[ans], sep='\n')