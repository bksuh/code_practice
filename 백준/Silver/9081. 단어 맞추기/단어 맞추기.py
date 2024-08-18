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
    return word
for _ in range(n):
    word = list(input().rstrip())
    ans = ''.join(next(word))
    print(ans)