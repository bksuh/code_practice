score = [6,3,2,1,2]
ans1, ans2 = 0, 0

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(len(arr1)):
    ans1 += (arr1[i] * score[i])
    ans2 += (arr2[i] * score[i])
    
print(ans1, ans2)