counts = {}
n = int(input())
t = input()

for i in range(len(t)):
    if t[i] ==' ' or t[i] ==',' or t[i] =='.':
        continue
    if t[i] in counts.keys():
        counts[t[i]] +=1
    else:
        counts[t[i]] = 1
count = counts.values()
print(max(count))