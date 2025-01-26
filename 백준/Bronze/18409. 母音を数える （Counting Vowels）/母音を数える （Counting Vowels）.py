vow = ['a', 'i', 'u', 'e', 'o']

ans = 0
t = int(input())
tar = input()

for v in vow:
    ans += tar.count(v)
print(ans)