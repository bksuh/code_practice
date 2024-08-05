tar = input()
lower = tar.lower()
left = ['q', 'w', 'e','r','t','y','a', 's','d','f','g','z','x','c','v','b']
left_cnt, right_cnt = 0, 0
cnt = 0
for c in tar:
    if c.isupper():
        cnt +=1
for c in lower:
    if c in left:
        left_cnt += 1
    elif c == ' ':
        cnt += 1
    else:
        right_cnt += 1

while cnt != 0:
    if left_cnt <= right_cnt:
        left_cnt += 1
    else:
        right_cnt +=1
    cnt -=1

print(left_cnt, right_cnt)