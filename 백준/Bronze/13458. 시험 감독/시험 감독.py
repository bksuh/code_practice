n = int(input())
classes = list(map(int, input().split()))
b, c = map(int, input().split())

ans = len(classes)
for i in range(len(classes)):
    if classes[i] - b >= 0:
        classes[i] = classes[i] - b
    else:
        classes[i] = 0
    left = classes[i] % c
    ans += classes[i] // c

    if left:
        ans += 1
    else:
        continue
print(ans)