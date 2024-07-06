a, b = 2, 18
x = int(input())
y = int(input())

if x==a and y==b:
    print("Special")
elif x<a or (x==a and y<b):
    print('Before')
else:
    print('After')