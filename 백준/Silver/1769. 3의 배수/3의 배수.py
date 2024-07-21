tar = input()
cnt = 0
while True:
    if len(tar) == 1:
        break
    tmp = list(int(c) for c in tar)
    tar = str(sum(tmp))
    cnt +=1

print(cnt)
if int(tar) %3 ==0:
    print("YES")
else: print("NO")