r = int(input())

room = [[1]*14 for _ in range(15)]
room[0] = [i for i in range(1, 15)]
for i in range(15):
    for j in range(14):
        if j == 0:
            room[i][j] = 1
        else:
            room[i][j] = room[i-1][j] + room[i][j-1]

for _ in range(r):
    k = int(input())
    n = int(input())
    print(room[k][n-1])