a = int(input())
for _ in range(a):
    h, w, n = map(int, input().split())
    floor = n % h
    room_num =(n//h)+1
    if floor ==0:
        floor = h
        room_num -=1
    print(floor*100+room_num)