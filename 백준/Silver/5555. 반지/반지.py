tar = input()
n = int(input())
cnt = 0
for _ in range(n):
    what = input()
    for i in range(len(what)):
        chan = what[i::] + what[0:i]
        if tar in chan:
            cnt+=1
            break
print(cnt)