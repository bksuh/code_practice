n = int(input())
for _ in range(n):
    d = {'TTT':0, 'TTH':0, 'THT':0, 'THH':0, 'HTT':0, 'HTH':0, 'HHT':0, 'HHH':0}
    result = input()
    for i in range(len(result)-2):
        tmp = result[i:i+3]
        d[tmp] +=1
    ans = list(d.values())
    print(*ans)