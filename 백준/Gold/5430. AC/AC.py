import collections
import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    commands = input().rstrip()
    t = int(input())
    arr = input().rstrip()
    if arr == '[]' :
        arr=collections.deque()
    else:
        arr=collections.deque(map(int, arr.rstrip(']').lstrip('[').split(',')))
    indi = True
    what = True
    for command in commands:
        if command == 'R':
            if indi:
                indi = False
            else:
                indi = True
        elif command == 'D':
            if not arr:
                print('error')
                what = False
                break
            if indi:
                arr.popleft()
            else:
                arr.pop()
            
    if arr:
        if indi:
            print('[', end ='')
            print(*arr, sep=',', end ='')
            print(']')
        else:
            print('[', end ='')
            print(*(reversed(arr)), sep=',', end='')
            print(']')    
        what = False
        
    if what:
        print('[]')