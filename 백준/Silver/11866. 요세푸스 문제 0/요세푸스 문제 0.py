import sys

n, k = map(int, sys.stdin.readline().split())
def answer(n, k):
    queue = list(i for i in range(1, n+1))
    res =[]
    idx =0
    while queue:
        idx +=k-1
        if idx >=len(queue):
            idx %= len(queue)
        res.append(queue.pop(idx))
    ans = "<"+str(res).strip('['']')+'>'
    return ans

print(answer(n,k))