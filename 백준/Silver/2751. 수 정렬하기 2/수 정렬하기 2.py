import sys
n = int(sys.stdin.readline())
arr=[]
for _ in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)
arr.sort()
for element in arr:
    print(element)