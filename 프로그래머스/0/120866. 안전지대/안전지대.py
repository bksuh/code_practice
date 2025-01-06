from collections import deque
dx, dy = [1, 1, 0, -1, -1, -1, 0, 1], [0, -1, -1, -1, 0, 1, 1, 1]

def bfs(board, result, queue):
    while queue:
        cx, cy = queue.popleft()
        result[cx][cy] = 1
        for k in range(len(dx)):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
                continue
            if result[nx][ny] == 1:
                continue
            else:
                result[nx][ny] = 1
    return result

def solution(board):
    queue = deque()
    result = []
    for _ in range(len(board)):
        tmp = [0 for _ in range(len(board[0]))]
        result.append(tmp)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                queue.append((i, j))
    result = bfs(board, result, queue)
    print(result)
    answer = 0
    for i in range(len(board)):
        answer += result[i].count(0)
    return answer