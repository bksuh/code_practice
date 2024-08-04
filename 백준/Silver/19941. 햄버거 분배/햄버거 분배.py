n, k = map(int, input().split())
arr = list(input())
cnt = 0

for i in range(n):
    if arr[i] != 'P':
        continue
    for j in range(i-k, i+k+1):
        if 0 <= j < n:
            if arr[j] == 'H':
                arr[j] = '-'
                cnt += 1
                break

print(cnt)