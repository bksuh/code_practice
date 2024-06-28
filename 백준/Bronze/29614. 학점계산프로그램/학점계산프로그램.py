d = {'A+':4.5 , 'A': 4.0, "B+":3.5, "B":3.0, "C+":2.5, "C": 2.0, "D+":1.5, "D": 1.0, "F":0.0}
arr = []
s = list(input())
for i in range(len(s)):
    if s[i] =='+':
        arr.pop(-1)
        tmp = s[i-1]+s[i]
        arr.append(tmp)
    else:
        arr.append(s[i])
total = 0
for i in range(len(arr)):
    total +=d[arr[i]]
print(total/len(arr))