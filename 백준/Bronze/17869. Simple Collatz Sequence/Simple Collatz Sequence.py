t = int(input())
cnt = 0
while True:
    if t == 1:
        break
    cnt +=1
    if t % 2 == 0:
         t//=2
    else:
        t += 1

print(cnt)