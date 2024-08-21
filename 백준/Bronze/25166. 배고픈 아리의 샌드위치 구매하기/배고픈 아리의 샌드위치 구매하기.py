a, b = map(int, input().split())
total = int("1111111111", 2)
if a <= total:
    print("No thanks")
elif (a-total) & b == (a-total):
    print("Thanks")
else:
    print("Impossible")