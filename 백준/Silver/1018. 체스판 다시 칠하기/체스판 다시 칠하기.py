n, m = map(int, input().split())
board = [input() for _ in range(n)]

chess =[
    'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
]
ans = []
for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if board[i+k][j+l] != chess[k][l]:
                    cnt += 1
        ans.append(min(cnt, 64-cnt))
print(min(ans))