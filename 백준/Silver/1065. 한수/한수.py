t = int(input())

cnt = 0
for i in range(1, t+1):
    tmp = [int(c) for c in str(i)]

    if len(tmp) < 3:
        cnt+=1
    else:
        gap = tmp[1] - tmp[0]
        indi = True
        for j in range(1, len(tmp)):
            if tmp[j]- tmp[j-1] != gap:
                indi = False
                break
        if indi:
            cnt+=1
print(cnt)