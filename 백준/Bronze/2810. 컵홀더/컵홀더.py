n = int(input())
tar = input()

tar = tar.replace("LL", "S")
cups = len(tar)+1
if cups >= n:
    ans = n
else:
    ans = cups
print(ans)