n = int(input())
m = int(input())
tar = input()
cnt = 0
find = 'I'+("OI"*n)
for i in range(m-len(find)+1):
    tmp = tar[i:i+len(find)]
    if tmp == find:
        cnt+=1

print(cnt)