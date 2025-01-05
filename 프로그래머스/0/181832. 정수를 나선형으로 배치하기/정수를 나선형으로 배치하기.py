
def solution(n):
    answer = [[0]*n for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    cx, cy = 0, 0
    way = 0
    ans = 1
    while ans <= n*n:
        answer[cx][cy] = ans
        ans += 1
        
        nx = cx + dx[way]
        ny = cy + dy[way]
        
        if  nx>=n or ny>=n or nx<0 or ny<0 or answer[nx][ny] != 0:
            way = (way+1)%4
            nx = cx + dx[way]
            ny = cy + dy[way]
        cx, cy = nx, ny
    return answer