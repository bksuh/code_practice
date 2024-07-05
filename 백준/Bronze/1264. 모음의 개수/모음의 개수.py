mo = ['a','e','i','o','u','A', 'E', 'I', 'O', 'U']

while True:
    target = input()
    if target == '#':
        break
    cnt = 0
    for elem in target:
        if elem in mo:
            cnt+=1
    print(cnt)