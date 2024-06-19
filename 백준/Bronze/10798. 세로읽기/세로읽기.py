ans = []
max_len = 0
for _ in range(5):
    tmp = input()
    max_len = max(len(tmp), max_len)
    ans.append(tmp)


for i in range(max_len):
    for j in range(5):
        if i>=len(ans[j]):
            continue
        print(ans[j][i], end ='')