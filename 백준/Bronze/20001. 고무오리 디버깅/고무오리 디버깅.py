start = input()
cnt = 0
while True:
    tmp = input()
    if tmp == '고무오리 디버깅 끝':
        break
    if tmp == '문제':
        cnt += 1
    elif cnt == 0 and tmp == '고무오리':
        cnt += 2
    else:
        cnt -= 1
if cnt == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")