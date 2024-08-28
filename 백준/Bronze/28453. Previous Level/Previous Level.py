n = int(input())
arr = list(map(int, input().split()))
tmp = [0]*n

def check(score):
    if score >= 300:
        return 1
    elif score >= 275:
        return 2
    elif score >= 250:
        return 3
    else:
        return 4
    
for i in range(len(arr)):
    tmp[i] = check(arr[i])

print(*tmp)