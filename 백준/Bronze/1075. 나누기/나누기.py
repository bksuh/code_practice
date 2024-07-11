n = input()
f = int(input())
n_tmp = n[:len(n)-2]
cnt = '0'
while True:

    if len(cnt) == 1:
        cnt = '0' +cnt
    ans = n_tmp + cnt
    if int(ans) % f == 0:
        print(ans[len(n)-2:])
        break
    cnt = str(int(cnt)+1)
