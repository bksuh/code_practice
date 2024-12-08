n, m = map(int, input().split())

if n >= m and m<=2:
    print("NEWBIE!")
elif n >= m :
    print("OLDBIE!")
else:
    print("TLE!")