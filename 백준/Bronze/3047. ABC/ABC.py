arr = list(map(int, input().split()))
arr.sort()

ans = input()
for c in ans:
    print(arr[ord(c)-ord('A')], end=' ')