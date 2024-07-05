arr = []
d = {}
for _ in range(10):
    tmp = int(input())
    arr.append(tmp)
cnt = set(arr)
for element in cnt:
    tmp = arr.count(element)
    if tmp in d.keys():
        d[tmp].append(element)
    else:
        d[tmp] =[element]
tmp = [(k,v) for k,v in d.items()]
tmp.sort(key= lambda x: (-x[0], x[1].sort(reverse=True)))

print(sum(arr)//10)
print(tmp[0][1][0])