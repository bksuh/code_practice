n = int(input())
arr = list(map(int, input().split()))
ans = []
for elem in arr:
    if elem == 0:
        ans.append(' ')
    elif 1 <= elem <= 26:
        ans.append(chr(ord('A')+elem-1))
    elif 27 <= elem <= 52:
        ans.append(chr(ord('a')+elem-27))
tar = [c for c in input()]
ans.sort()
tar.sort()

if ans == tar:
    print('y')
else:
    print('n')