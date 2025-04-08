arr = list(map(int, input().split()))
a, b, c = arr
if len(set(arr)) == 1:
    print("*")

elif a == b and a!= c:
    print("C")
elif a == c and a!=b:
    print("B")
else:
    print("A")