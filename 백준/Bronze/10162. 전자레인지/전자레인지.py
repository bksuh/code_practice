t = int(input())

a = t//300
t = t%300

b = t // 60
t = t % 60

c = t // 10
d = t % 10

if d == 0:
    print(a, b, c)
else:
    print(-1)