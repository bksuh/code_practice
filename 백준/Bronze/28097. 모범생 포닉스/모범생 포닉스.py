t = int(input())
arr = list(map(int, input().split()))

ans = sum(arr) + (t-1)*8
hr = ans // 24
mins = ans % 24

print(hr, mins)