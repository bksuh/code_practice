board = [list(map(int, input().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
x, y = map(int, input().split())
cnt = 0
move = 0
ans = False

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(row, col):
    global cnt, move, ans

    visited[row][col] = 1   
    if move == 1:         
        cnt = 0

    if move > 3:            
        move -= 1
        return
    else:
        move += 1         

    if board[row][col] == -1:    
        return
    elif board[row][col] == 1 and cnt <= 2:  
        cnt += 1

    if cnt >= 2:           
        ans = True

    for i in range(4):         
        dxow = row + dx[i]
        dyol = col + dy[i]
        if 0 <= dxow < 5 and 0 <= dyol < 5 and move == 1:   
            visited[dxow][dyol] = 0
        if 0 <= dxow < 5 and 0 <= dyol < 5 and visited[dxow][dyol] == 0 and move <= 3: 
            dfs(dxow, dyol) 
            move -= 1  
        else:
            continue
    return

dfs(x, y)

print(1 if ans else 0)