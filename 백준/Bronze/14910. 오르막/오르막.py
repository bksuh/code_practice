a = list(map(int, input().split()))
b = sorted(a)
print("Good" if a==b else "Bad")