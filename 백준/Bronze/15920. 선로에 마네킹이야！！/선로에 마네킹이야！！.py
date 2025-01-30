t = int(input())
commands = input()
pulled = False
check_indi = False
w_cnt = 0
ans = 0

for command in commands:
    if w_cnt == 0:
        if command == 'P':
            pulled = not pulled
        else:
            w_cnt += 1
    elif w_cnt == 1:
        if command == 'P':
            check_indi = True
        else:
            w_cnt += 1

if w_cnt >= 2 and ans == 0:
    if check_indi:
        ans = 6
    elif pulled:
        ans = 1
    else:
        ans = 5

print(ans)