N, M = map(int, input().split())
a = list(map(int, input().split()))	# 지금 시설
b = list(map(int, input().split()))	# 예전 시설

if N < M :
    a += [0] * (M-N)

result = 0
for i in range(M) :
    result = max(result, b[i] - a[i])

print(result)