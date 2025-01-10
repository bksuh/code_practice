t = int(input())
arr = list(map(int, input().split()))
tmp = [(i,v) for i, v in enumerate(arr)]

tmp1 = sorted(tmp, key=lambda x: (x[1], x[0]))
real  = {v:i for i, v in enumerate(tmp1)}

answer = []
for elem in tmp:
    answer.append(real[elem])
print(*answer)