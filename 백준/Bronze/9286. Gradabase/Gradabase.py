import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    m = int(input())
    print(f"Case {i+1}:")
    for _ in range(m):
        x = int(input())
        if x <= 5:
            print(x+1)
        else:
            continue