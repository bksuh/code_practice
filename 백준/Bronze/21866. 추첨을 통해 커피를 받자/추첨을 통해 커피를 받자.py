scores = list(map(int, input().split()))
totals = [101, 101, 201, 201, 301, 301, 401, 401, 501]
ans = False

if sum(scores) < 100:
    print('none')
else:
    for i in range(len(scores)):
        if scores[i] >= totals[i]:
            print('hacker')
            ans = True
            break
    if not ans:
        print('draw')