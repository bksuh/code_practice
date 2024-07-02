date = ['MON', 'TUE','WED', 'THU', 'FRI', 'SAT', 'SUN']
monthly_days = [0, 31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

m, d = map(int, input().split(' '))
ans = 0
for i in range(1, m):
    ans +=monthly_days[i]
ans += d-1
print(date[ans%7])