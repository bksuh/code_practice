arr =[]
for _ in range(3):
    arr.append(input())

for i, element in enumerate(reversed(arr)):
    if element.isdigit():
        ans = int(element) + i+ 1

if ans % 3 == 0 :
    print("Fizz", end='')
if ans % 5 == 0:
    print('Buzz')
if ans% 3 != 0 and ans%5 != 0:
    print(ans)