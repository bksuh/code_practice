val = []
for _ in range(5):
    score = list(map(int, input().split()))
    val.append(sum(score))

print(val.index(max(val))+1, max(val))