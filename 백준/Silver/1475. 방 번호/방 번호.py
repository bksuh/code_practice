import sys
input = sys.stdin.readline

arr = [0]*10
ans = [int(c) for c in input().rstrip()]

for i in range(len(ans)):
    if ans[i] == 6 or ans[i]== 9:
        if arr[6]> arr[9]:
            arr[9]+=1
        else:
            arr[6]+=1
    else:
        arr[ans[i]] +=1
print(max(arr))