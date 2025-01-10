t = int(input())
prices = list(map(int, input().split()))
possible = int(input())
start, end = 1, max(prices)

while start <= end:
    mid = (start+end)//2
    total = 0
    for price in prices:
        if price >= mid:
            total += mid
        else:
            total += price
    if total <= possible:
        start = mid + 1
    else:
        end = mid - 1
print(end)