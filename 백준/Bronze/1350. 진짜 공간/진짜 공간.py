n = int(input())

files = list(map(int, input().split()))
clust = int(input())

ans = 0

for file in files:
    if 0 < file <=clust:
        ans += 1
    elif file > clust:
        tmp = file // clust
        if file % clust > 0:
            tmp += 1
        ans += tmp
print(clust*ans)