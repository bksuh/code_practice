import sys
input = sys.stdin.readline

n = int(input())

def next(word):
    for i in range(len(word)-1, 0, -1):
        if word[i-1] < word[i]:
            for j in range(len(word)-1, i-1, -1):
                if word[i-1] < word[j]:
                    word[i-1], word[j] = word[j], word[i-1]
                    return(word[:i] + word[i:][::-1])
    return -1
arr = list(map(int, input().split()))
ans = next(arr)
if ans != -1:
    print(*ans)
else:
    print(-1)