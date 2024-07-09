n = int(input())
for _ in range(n):
    t = int(input())
    if t==1:
        print('#')
        print()
    else:
        print('#'*t)
        for _ in range(t-2):
            print('#'+'J'*(t-2)+'#')
        print('#'*t)
        print()