N, K = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(N)]

for row in image:
    for _ in range(K):
        expanded_row = [] 
        for pixel in row:
            for _ in range(K):
                expanded_row.append(pixel)
        print(*expanded_row)