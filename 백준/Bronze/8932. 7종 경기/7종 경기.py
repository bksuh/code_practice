d = {0:[9.23076, 26.7, 1.835,'track'], 
     1:[1.84523,	75,	1.348,'field'],
     2:[56.0211,	1.5,	1.05,'field'],
     3:[4.99087,	42.5,	1.81,'track'],
     4:[0.188807,	210,	1.41,'field'],
     5:[15.9803,	3.8,	1.04,'field'],
     6:[0.11193,	254,	1.88,'track']
    }
import math
n = int(input())
for _ in range(n):
    score = 0
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if d[i][3] == 'track':
            score += math.floor(d[i][0]*pow(d[i][1]-arr[i],d[i][2]))
        elif d[i][3] == 'field':
            score += math.floor(d[i][0]*pow(arr[i]-d[i][1],d[i][2]))
    print(score)