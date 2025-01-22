a, b = map(int, input().split())
speeds = [0 for _ in range(100)]
idx = 0
for _ in range(a):
    s, e = map(int, input().split())
    for i in range(idx, idx + s):
        speeds[i] = e
    idx = idx + s
cnt = 0
idx = 0

for _ in range(b):
    s, e = map(int, input().split())
    for i in range(idx, idx + s):
        if speeds[i] <= e:
            cnt = max(cnt, e-speeds[i])
    idx = idx + s
print(cnt)