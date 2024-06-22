n = input()

grid = [0]*(ord('z')-ord('a')+1)

for c in n:
    grid[ord(c)-ord('a')]+=1

print(*grid)
    