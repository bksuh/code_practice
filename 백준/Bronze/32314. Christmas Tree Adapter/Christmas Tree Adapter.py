a = int(input())
w, v = map(int, input().split())
t = w//v

if t >= a:
    print(1)
else:
    print(0)