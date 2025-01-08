t = int(input())
coup = []

for _ in range(t):
    _ , d = input().split('-')
    d = int(d)
    coup.append(d)

cnt = 0
for elem in coup:
    if elem <= 90:
        cnt += 1
print(cnt)