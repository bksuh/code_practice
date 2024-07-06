arr=['a','e','i','o','u']
tar = input()
cnt =0
for i in tar:
    if i in arr:
        cnt+=1

print(cnt)