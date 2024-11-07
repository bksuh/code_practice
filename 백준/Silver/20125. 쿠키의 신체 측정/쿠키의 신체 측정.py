t = int(input())
grid = []
for _ in range(t):
    tmp = [c for c in input()]
    grid.append(tmp)

for i in range(1, t-1):
    for j in range(1, t-1):
        if grid[i][j-1: j+2] == ['*', '*', '*'] and grid[i-1][j]=='*' and grid[i+1][j]=='*':
            body_x, body_y = i, j
print(body_x+1, body_y+1)

arm_start = grid[body_x].index('*')
left_arm = body_y - arm_start
right_arm = grid[body_x].count('*') - left_arm - 1
body_len = 0
for i in range(body_x+1, t):
    if grid[i][body_y] == '*':
        body_len += 1
        last_body = i
left_leg, right_leg = 0, 0
for i in range(last_body, t):
    if grid[i][body_y-1] =='*':
        left_leg +=1
    if grid[i][body_y+1] =='*':
        right_leg +=1
        
print(left_arm, right_arm, body_len, left_leg, right_leg)