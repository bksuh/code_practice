t = int(input())
arr = list(map(int, input().split()))
odd, even = 0, 0

for num in arr:
    if num%2 == 0:
        even +=1
    else:
        odd +=1

if even > odd:
    print("Happy")
else:
    print('Sad')