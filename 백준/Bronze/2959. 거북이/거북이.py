arr = list(map(int, input().split()))
arr.sort()
w, h = [arr[-1], arr[-2]], [arr[0], arr[1]]

print(min(w)*min(h))