name = input()
n = int(input())
if n == 1:
    print(input())
else:
    picks = ["L", 'O', 'V', 'E']
    result = {c: name.count(c) for c in picks}
    result_cnt = [int(c) for c in result.values()]
    teams = []
    for _ in range(n):
        tar = input()
        d = {c:tar.count(c) for c in picks}
        d_cnt = [int(c) for c in d.values()]
        ans = []
        for i in range(len(d_cnt)):
            ans.append(result_cnt[i]+d_cnt[i])
        score = 1
        for i in range(len(ans)-1):
            for j in range(i+1, len(ans)):
                score *= ans[i]+ans[j]
        teams.append((score%100, tar))
    teams.sort(key=lambda x: (-x[0], x[1]))
    print(teams[0][1])