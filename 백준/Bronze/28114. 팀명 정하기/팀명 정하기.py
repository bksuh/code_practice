teams = []
for _ in range(3):
    p, y, s = input().split()
    p, y = int(p), int(y)%100
    teams.append((p, y, s))
    
teams.sort(key = lambda x: x[1])
name1 = ''
for i in range(3):
    name1 += str(teams[i][1])
print(name1)

teams.sort(key = lambda x: -x[0])
name2 = ''
for i in range(3):
    name2 += teams[i][2][0]
print(name2)