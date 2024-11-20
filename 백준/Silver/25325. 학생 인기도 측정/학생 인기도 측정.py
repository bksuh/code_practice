t = int(input())
names = list(input().split())
picks = {}
for name in names:
    picks[name] = 0
    
for i in range(t):
    sample = list(input().split())
    for name in sample:
        if name == names[i]:
            continue
        if name in picks.keys():
            picks[name] +=1
        else:
            picks[name] = 1
result = [(k,v) for k,v in picks.items()]
result.sort(key= lambda x: (-x[1],x[0]))
for name, vote in result:
    print(name, vote)