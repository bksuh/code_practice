n = int(input())
dist = list(map(int, input().split()))
gas = list(map(int, input().split()))

import sys
tmp = sys.maxsize
result = [tmp]*n
result[0] = 0

for i in range (len(gas)-1):
    current_price = gas[i]
    for j in range(len(dist)):
        distance_target = sum(dist[i:j+1])
        if distance_target == 0:
            continue
        else:
            tmp = current_price * distance_target
            result[j+1] = min(result[j+1], result[i]+ tmp)
print(result[-1])