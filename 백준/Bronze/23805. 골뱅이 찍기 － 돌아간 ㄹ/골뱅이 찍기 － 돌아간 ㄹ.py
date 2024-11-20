t = int(input())
for _ in range(t):
    print('@@@'*t +' '*t + '@'*t)

for _ in range(3*t):
    print('@'*t + ' '*t + '@'*t + ' '*t + '@'*t)

for _ in range(t):
    print('@'*t + ' '*t + '@@@'*t)