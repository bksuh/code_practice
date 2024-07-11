n = int(input())
for _ in range(n):
    x, y = input().split()
    if y == 'C':
        arr = list(input().split())
        for element in arr:
            print(ord(element)-ord('A') +1, end=' ')
        print()
    else:
        arr = list(map(int, input().split()))
        for element in arr:
            print(chr(ord('A')+element-1), end=' ')
        print()