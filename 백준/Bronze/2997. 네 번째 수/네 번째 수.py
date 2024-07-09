arr= list(map(int, input().split()))
arr.sort()
a, b, c = arr

if b-a == c-b:
    m = 2*c - b
else:
    m = 2*b-a
    if c-m == b-a:
        m = 2*b - a
    else:
        m = (b+a)//2
print(m)