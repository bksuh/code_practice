n = int(input())
cnt = 0
for i in range(1, 501):
    for j in range(i+1, 501):
        if pow(i,2) + n == pow(j,2):
            cnt += 1
print(cnt, end='')