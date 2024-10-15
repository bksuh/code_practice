t = int(input())

days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(t):
    x, y = map(int, input().split())
    time , date = 'No', 'No'
    if 0 <= x <= 23 and 0<= y<= 59:
        time = 'Yes'
    if 1<= x<= 12 and 1 <=y <= days[x]:
        date = 'Yes'
    print(time, date)