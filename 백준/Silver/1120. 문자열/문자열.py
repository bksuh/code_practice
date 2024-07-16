a, b = input().split()
score = 0
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            score += 1
elif a in b:
    score = 0
else:
    ans = []
    for i in range(len(b)-len(a)+1):
        tmp = b[i:i+len(a)]
        score = 0 
        for i in range(len(a)):
            if tmp[i] != a[i]:
                score += 1
        ans.append(score)
    score = min(ans)

print(score)