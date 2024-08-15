students = [0, 0, 0, 0]
n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == 1:
        students[3] += 1
    else:
        if b == 1 or b == 2:
            students[0] += 1
        elif b == 3 :
            students[1] += 1
        else:
            students[2] += 1
print(*students, sep='\n')