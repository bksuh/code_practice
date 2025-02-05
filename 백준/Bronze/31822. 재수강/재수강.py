subject = input()
subject_code = subject[:5]
n = int(input())

cnt = 0

for _ in range(n):
    classes = input()
    classes_code = classes[:5]
    if classes_code == subject_code:
        cnt += 1

print(cnt)