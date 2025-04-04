t = int(input())

for _ in range(t):
    s, a = map(int, input().split())
    s = s - (a//7)
    s = s + (a//4)
    print(s)