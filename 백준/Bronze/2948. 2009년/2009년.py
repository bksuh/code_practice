day = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
date = ['Wednesday','Thursday', 'Friday', 'Saturday','Sunday', 'Monday', 'Tuesday']
d, m = map(int, input().split())

tmp = day[m-1] + d
print(date[tmp%7])