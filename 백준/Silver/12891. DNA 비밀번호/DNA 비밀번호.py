n, k = map(int, input().split())
possible = input()
indi = list(map(int, input().split()))
tmp = possible[0:k]
current = {'A' : tmp.count('A'), 'C': tmp.count('C'), 'G':tmp.count('G'), 'T':tmp.count('T')}
state = list(current.values())
if indi[0] > state[0] or indi[1] > state[1] or indi[2] > state[2] or indi[3] > state[3]:
    ans = 0
else:
    ans = 1

for i in range(n-k):
    current[possible[i]] -= 1
    current[possible[i+k]] += 1
    state = list(current.values())
    if indi[0] > state[0] or indi[1] > state[1] or indi[2] > state[2] or indi[3] > state[3]:
        continue
    else:
        ans +=1

print(ans)