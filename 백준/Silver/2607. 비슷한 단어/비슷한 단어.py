t = int(input())
target = input()
ans = 0

for _ in range(t-1):
    picks = [c for c in input()]
    indi = False
    cnt = 0
    if len(target) == len(picks) or len(picks) -1 == len(target) or len(picks)+1==len(target):
        indi = True
    for tar in target:
        try:
            picks.remove(tar)
        except:
            cnt += 1
    if len(picks) <= 1 and indi and cnt < 2:
        ans += 1
print(ans)