n = int(input())
arr = []
counter = {}
for _ in range(n):
    t = int(input())
    arr.append(t)
    if t in counter:
        counter[t] +=1
    else:
        counter[t] = 1
#산술평균
print(round(sum(arr)/len(arr)))
#중앙값
arr.sort()
print(arr[n//2])
#최빈값
tar = max(counter.values())
tmp = []
for k, v in counter.items():
    if v != tar:
        continue
    else:
        tmp.append(k)
tmp.sort()
if len(tmp) > 1:
    print(tmp[1])
else:
    print(tmp[0])
#범위
print(arr[-1]-arr[0])