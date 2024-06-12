import sys

n = int(sys.stdin.readline())
arr=[]

for _ in range(n):
    tmp = tuple(sys.stdin.readline().split())
    if tmp[0] == 'push':
        arr.append(int(tmp[1]))
    
    elif tmp[0] == 'pop':
        if len(arr) != 0:
            print(arr.pop())
        else:
            print(-1)
    elif tmp[0] == 'size':
        print(len(arr))

    elif tmp[0] == 'empty':
        if len(arr) ==  0:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'top':
        if len(arr) !=0:
            print(arr[-1])
        else:
            print(-1)