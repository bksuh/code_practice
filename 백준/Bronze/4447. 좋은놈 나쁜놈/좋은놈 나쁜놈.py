n = int(input())

for _ in range(n):
    target = input()
    tmp = target.lower()
    g = tmp.count('g')
    b = tmp.count('b')
    if g > b:
        print(f"{target} is GOOD")
    elif g < b:
        print(f"{target} is A BADDY")
    else:
        print(f"{target} is NEUTRAL")