n = int(input())

def next():
    ans = list(int(c) for c in input())
    for i in range(len(ans)-1, 0, -1):
        if ans[i] > ans[i-1]:
            for j in range(len(ans)-1, i-1, -1):
                if ans[j] > ans[i-1]:
                    ans[j], ans[i-1] =ans[i-1], ans[j]
                    real = ans[:i] + ans[i:][::-1]
                    return real
    return "BIGGEST"

for _ in range(n):
    ans = next()
    if ans == "BIGGEST":
        print(ans)
    else:
        print(*ans, sep='')