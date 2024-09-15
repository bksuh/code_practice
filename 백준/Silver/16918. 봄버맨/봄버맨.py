n, m, t = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]


dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def explode(grid):
    new_grid = [['O'] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                new_grid[i][j] = '.'
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        new_grid[nx][ny] = '.'
    return new_grid

if t == 1:
    result = grid
elif t % 2 == 0:
    result = [['O'] * m for _ in range(n)]
else:
    first_explosion = explode(grid)
    if (t // 2) % 2 == 1:
        result = first_explosion
    else:
        result = explode(first_explosion)

for row in result:
    print(''.join(row))
